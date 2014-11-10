var newshare;
var newblock;

function playNewShareSound() {
    newshare = $("#audio-newshare")[0];

    if (newshare && newshare.play) {
        newshare.play();
    }        
}

function playNewBlockSound() {
    newblock = $("#audio-newblock")[0];

    if (newblock && newblock.play) {
        newblock.play();
    }        
}

var currency, currency_info, rate, local_stats,
    global_stats, current_payouts, 
    recent_blocks, current_block, last_block,
    recent_shares, current_share, last_share,
    payout_addr, getwork_latency;

var local_hashrate= 0, local_doa_hashrate= 0;

// init
$(document).on('init', function(e, eventInfo) {
  initAudio();
  fetchdata();
  fetchBlocks();
  fetchBitcoind();
  fetchBlockchainInfo();
  fetchGraph('day');
  updateLatency();
});

$(document).on('update', function(e, eventInfo) {
  rotateAd();
  fetchdata();
  fetchBlocks();
  fetchBitcoind();
  fetchBlockchainInfo();
});

$(document).on('update_graph', function(e, eventInfo) {
  fetchGraph('day');
  updateLatency();
});

// Fills the list of active miners on this node.

$(document).on('update_miners', function(e, eventInfo) {
  local_hashrate= 0; local_doa_hashrate= 0; local_payout = 0;
  $.each(local_stats.miner_hash_rates, function(address, hashrate) {
    tr= $('<tr/>').attr('id', address);

    // highlight our miner if configured
    if(config.myself && config.myself.length > 0 &&
       $.inArray(address, config.myself) >= 0) {
      tr.addClass('warning');
    }

    local_payout += current_payouts[payout_addr] || 0;

    var address_link= $('<a/>')
      .attr('href', 'miner.html#' + address)
      .text(address);

    address_span= $('<span/>').addClass('coin_address').append(address_link);

    doa = local_stats.miner_dead_hash_rates[address] || 0;
    doa_prop = (parseFloat(doa) / parseFloat(hashrate)) * 100;

    local_hashrate += hashrate || 0;
    local_doa_hashrate += doa  || 0;

    tr.append($('<td/>').addClass('text-left')
      .append(address_span)
      .append('&nbsp;'));
    tr.append($('<td/>').addClass('text-right')
      .append(formatHashrate(hashrate)));
    tr.append($('<td/>').addClass('text-right')
      .append(formatHashrate(doa)));
    tr.append($('<td/>').addClass('text-right')
      .append(doa_prop.toFixed(2) + '%'));

    payout= current_payouts[address] || 0;

    if (payout) {
      td= $('<td/>').attr('class', 'text-right');
      button = $('<button class="to_usd"/>');
      span = $('<span id="payout-' + address + '"/>')
        .attr('data-value', payout)
        .text(parseFloat(payout).toFixed(8))
        .append(' ').append(currency.clone());
      button.append(span);
      td.append(button);
      tr.append(td);
    }
    else {
      tr.append($('<td/>').attr('class', 'text-right')
        .append($('<i/>').append('no shares yet')));
    }
    $('#'+address).remove(); 
    $('#active_miners').append(tr);
  });

  var rows = $('#active_miners tbody tr').get();
  rows.sort(function(a, b) {
      // eq(4) gives us column 5 (the payout column)
      var A = $(a).children('td').eq(4).text();
      var B = $(b).children('td').eq(4).text();

      if(A == 'no shares yet') { return 1; }
      if(B == 'no shares yet') { return -1; }
      if(A > B) { return -1; }
      if(A < B) { return 1;  }
      return 0;
  });

  // replace the rows with the sorted ones
  $.each(rows, function(index, row) {
    $('#active_miners').children('tbody').append(row);
  });

  if (local_payout !== 0) {
    $('#payout_now')
      .text(local_payout)
      .append(' ')
      .append(currency.clone());
    $('#payout_now').attr('data-value', local_payout);
  } else {
    $('#payout_now').html('&dash;');
  }

  if(local_doa_hashrate !== 0 && local_hashrate !== 0) {
    doa_rate= (local_doa_hashrate / local_hashrate) * 100;
  } else { doa_rate= 0; }

  rate= formatHashrate(local_hashrate)
    + ' (DOA '
    + formatHashrate(local_doa_hashrate)
    + ' / ' + doa_rate.toFixed(2)
    + '%)';
  $('#local_rate').text(rate);

  pool_hash_rate=
    parseInt(global_stats.pool_hash_rate || 0);
  pool_nonstale_hash_rate=
    parseInt(global_stats.pool_nonstale_hash_rate || 0);
  global_doa_rate= pool_hash_rate - pool_nonstale_hash_rate;

  global_rate= formatHashrate(pool_hash_rate)
    + ' (DOA '
    + formatHashrate(global_doa_rate)
    + ' / ' + ((global_doa_rate / pool_hash_rate) * 100).toFixed(2)
    + '%)';
  $('#global_rate').text(global_rate);

  $('#share_difficulty')
    .text(addCommas(parseFloat(global_stats.min_difficulty).toFixed(2)));

  $('#block_value')
    .attr('data-value', parseFloat(local_stats.block_value).toString())
    .text(parseFloat(local_stats.block_value).toFixed(8).toString() + ' ' + currency_info.symbol);

  $('#efficiency')
  .text(parseFloat(local_stats.efficiency * 100).toFixed(2) + '%');
  $('#node_fee')
    .text(local_stats.fee + '%');
  $('#node_donation')
    .text((local_stats.donation_proportion * 100) + '%');
  $('#p2pool_version')
    .text(local_stats.version);
  $('#protocol_version')
    .text(local_stats.protocol_version);

  $('#peers_in').text(local_stats.peers.incoming);
  $('#peers_out').text(local_stats.peers.outgoing);

  $('#node_uptime').text(('' + local_stats.uptime).formatSeconds());

  if(local_stats.warnings.length > 0) {
    $('#node_alerts').empty();

    $.each(local_stats.warnings, function(key, warning) {
      $('#node_alerts').append($('<p/>').append(warning));
    });

    $('#node_alerts').fadeIn(1000, function() {
      $(this).removeClass('hidden');
    });
  }

  $('#shares')
    .text('Total: ' + (local_stats.shares.total - local_stats.shares.unknown)
    + ' (Orphan: ' + local_stats.shares.orphan
    + ', Dead: ' + local_stats.shares.dead + ')');

  if(local_hashrate !== 0) {
    time_to_share=
      (parseInt(local_stats.attempts_to_share) / parseInt(local_hashrate));
    $('#expected_time_to_share').text((''+time_to_share).formatSeconds());
  } else {
    $('#expected_time_to_share').html('&dash;');
  }

  attempts_to_block=
    parseInt(local_stats.attempts_to_block || 0);
  time_to_block= attempts_to_block / pool_hash_rate;
  $('#expected_time_to_block').text((''+time_to_block).formatSeconds());

  bindCurrencyConversionButtons();
});

// Fills the recent block table

$(document).on('update_blocks', function(e, eventInfo) {
  var table = document.getElementById("recent_blocks");
  for (var i = table.rows.length - 1; i > 0; i--) {
    table.deleteRow(i);
  }

  current_block = recent_blocks[0]['share'];
  if (last_block == null) { last_block = current_block; }
  if (current_block != last_block) {
    if (config.enable_audio) {
      playNewBlockSound();
    }

    var new_block_link = $('<a/>')
      .attr('href', 'block.html#' + current_block)
      .text('New block found! ' + current_block);
    $('#node_alerts').empty();
    $('#node_alerts').append(new_block_link);
    $('#node_alerts').removeClass('hidden');         
  }
  last_block = current_block;

  $.each(recent_blocks, function(key, block) {
    ts= block.ts; num= block.number; hash= block.hash;

    blockinfo= $('<a/>').attr('href', 'block.html#' + hash).text(hash);

    // synchronously lookup confirmations for the block
    var confirmations = '&dash;';

    try {
        $.ajax('/bitcoind/block/' + hash, {
            async: false,
            success: function(data) {
                if (data) {
                    confirmations = data['confirmations'];
                }
            }
        });
    } catch(error) {
        // do nothing -- use default of &dash
    }

    tr= $('<tr/>').attr('id', num);
    tr.append($('<td/>')
      .append($.format.prettyDate(new Date(ts * 1000))));
    tr.append($('<td/>').append(num));
    tr.append($('<td/>').append(blockinfo));
    tr.append($('<td/>').addClass('text-center').html(confirmations));
    $('#'+num).remove(); $('#recent_blocks').append(tr);
  });
});

$(document).on('update_shares', function(e, eventInfo) {
  var table = document.getElementById("recent_shares");
  for (var i = table.rows.length - 1; i > 0; i--) {
    table.deleteRow(i);
  }
  
  $.each(recent_shares, function(key, block) {
    hash = block;

    blockinfo= $('<a/>')
      .attr('href', 'share.html#' + hash).text(hash);

    var shareinfo;
    $.ajax('/web/share/' + hash, {
        async: false,
        success: function(data) {
            if (data) {
                shareinfo = data['share_data'];
            }
        }
    });

    if (shareinfo) {
      var address_link= $('<a/>')
        .attr('href', 'miner.html#' + shareinfo.payout_address)
        .text(shareinfo.payout_address);

      var stale_info = $('<span/>');
      if (shareinfo.stale_info == null) {
        stale_info.addClass('green').text('valid');
      } else {
        stale_info.addClass('red').text(shareinfo.stale_info);
      }

      tr= $('<tr/>').attr('id', hash);

      if(config.myself && config.myself.length > 0 && $.inArray(shareinfo.payout_address, config.myself) >= 0) {
        tr.addClass('warning');
      }

      tr.append($('<td class="hidden"/>').text(shareinfo.timestamp));
      tr.append($('<td/>').text($.format.prettyDate(new Date(shareinfo.timestamp * 1000))));
      tr.append($('<td/>').append(blockinfo));
      tr.append($('<td/>').append(address_link));
      tr.append($('<td/>').addClass('text-center').append(stale_info));
      $('#recent_shares tbody').append(tr);
    }
  });

  var rows = $('#recent_shares tbody tr').get();
  rows.sort(function(a, b) {
      // eq(0) gives us column 1 (the hidden timestamp column)
      var A = parseFloat($(a).children('td').eq(0).text());
      var B = parseFloat($(b).children('td').eq(0).text());

      if(A > B) { return -1; }
      if(A < B) { return 1;  }
      return 0;
  });

  // replace the rows with the sorted ones
  $.each(rows, function(index, row) {
    $('#recent_shares').children('tbody').append(row);
  });

  paginateTable($('#recent_shares')[0]);

  // notification for share change
  // since recent_shares are returned in an abitrary order, we had to wait for sorting before checking for the most recent
  current_share = $('#recent_shares').children('tbody').children('tr').first().attr('id');
  if (last_share == null) { last_share = current_share; }
  if (current_share != last_share && current_share != null) {
    if (config.enable_audio) {
      playNewShareSound();
    }

    var new_share_link = $('<a/>')
      .attr('href', 'share.html#' + current_share)
      .text('New share found! ' + current_share)
    $('#node_alerts').empty();
    $('#node_alerts').append(new_share_link);
    $('#node_alerts').removeClass('hidden');
  }
  last_share = current_share;
});

// Place the currency symbol for the currency the node is mining.  If
// it's Bitcoin, use the fontawesome BTC icon

var set_currency_symbol= true;
$(document).on('update_currency', function(e, eventInfo) {
  currency= $('<span/>').append(currency_info.symbol);

  if(set_currency_symbol) {
    $('#currency')
      .append('(').append(currency).append(')');
    set_currency_symbol= false;
  }
});

// Updates the 'Updated:' field in page header

$(document).on('update_time', function(e, eventInfo) {
  dts= $.format.date(new Date(), 'yyyy-MM-dd HH:mm:ss');
  $('title').text('P2Pool Node Status');
  $('#updated').attr('class', '').text('Updated: ' + dts);
});

$(document).on('update_bitcoind', function(e, eventInfo) {
  $('#network_rate')
    .text(formatHashrate(parseFloat(mining_info.networkhashps)));
  $('#blocks')
    .text(addCommas(mining_info.blocks));
  $('#bitcoind_uptime')
    .text(bitcoind_info.uptime);
  $('#block_difficulty')
    .text(addCommas(mining_info.difficulty));
  $('#current_block_size')
    .text(addCommas(mining_info.currentblocksize));
  $('#current_block_txs')
    .text(addCommas(mining_info.currentblocktx));
  $('#bitcoind_version')
    .text(bitcoind_info.version);
  $('#bitcoind_protocol')
    .text(bitcoind_info.protocolversion);

  inbound_status = $.map(bitcoind_peer_info, function(info, i) { return info['inbound']; });
  inbound_only = $.grep(inbound_status, function (elem) { return elem === true; }).length;

  $('#bitcoind_connections_in')
    .text(inbound_only);
  $('#bitcoind_connections_out')
    .text(inbound_status.length);

  connection_times = $.map(bitcoind_peer_info, function(info, i) { return info['conntime']; });
  earliest_connection = Math.min.apply(null, connection_times);
  up_since = new Date(earliest_connection * 1000);
  up_seconds = (new Date() - up_since)/1000;

  $('#bitcoind_uptime')
    .text(up_seconds.toString().formatSeconds());
  $('#bitcoind_relay_fee')
    .attr('data-value', bitcoind_info.relayfee)
    .text(bitcoind_info.relayfee.toString() + ' BTC');

  bitcoind_peer_pingtimes = $.map(bitcoind_peer_info, function(value, i) {
    ping = parseFloat(value['pingtime']);
    return (ping > 0 ? ping : null);
  });

  total = 0;
  for (var i = 0; i < bitcoind_peer_pingtimes.length; i++) {
      total += bitcoind_peer_pingtimes[i];
  }

  bitcoind_peer_avg_ping = (total / bitcoind_peer_pingtimes.length * 1e3);

  if (bitcoind_peer_avg_ping) {
    $('#bitcoind_peer_latency')
      .text(bitcoind_peer_avg_ping.toFixed(0).toString() + ' ms');
  } else {
    $('#bitcoind_peer_latency')
      .html('&dash;');    
  }
});

$(document).on('update_blockchain_info', function(e, eventInfo) {
  $('#total_bitcoins')
    .attr('data-value', total_bitcoins)
    .text(addCommas(total_bitcoins.toString()) + ' BTC');
  $('#block_interval')
    .text((''+block_interval).formatSeconds());
  $('#block_eta')
    .text((''+Math.abs(block_eta)).formatSeconds());

  if (block_eta < 0) {
    $('#block_eta').addClass('red bold').text('-' + $('#block_eta').text());
  } else {
    $('#block_eta').attr('class', '');
  }

  $('#block_probability')
    .text(parseFloat(block_probability) * 1e9).append('%');
  $('#hashes_to_win')
  .text(formatHashrate(hashes_to_win).replace('/s', ''));
});

// ==================================================================

var fetchdata= function() {
  $.getJSON('/rate', function(data) {
    if(data) rate= data;

    $.getJSON('/web/currency_info', function(data) {
      currency_info= data;
      $(document).trigger('update_currency');

      $.getJSON('/local_stats', function(data) {
        if(data) local_stats= data;

        $.getJSON('/current_payouts', function(data) {
          if(data) current_payouts= data;

          $.getJSON('/payout_addr', function(data) {
            if(data) payout_addr= data;

            $.getJSON('/global_stats', function(data) {
              if(data) global_stats= data;

              $(document).trigger('update_miners');
              $(document).trigger('update_time');
            });
          });
        });
      });
    });
  });
};

var fetchBlocks= function() {
  $.getJSON('/web/currency_info', function(data) {
    currency_info= data;
    $.getJSON('/recent_blocks', function(data) {
      if(data) recent_blocks= data;
      $(document).trigger('update_blocks');
    });
    $.getJSON('/web/my_share_hashes', function(data) {
      if(data) recent_shares= data;
      $(document).trigger('update_shares');
    });
  });
}

var bitcoind_info, mining_info, bitcoind_peer_info;
var fetchBitcoind = function() {
  $.getJSON('/bitcoind/getinfo', function(data) {
    bitcoind_info = data;

    $.getJSON('/bitcoind/getmininginfo', function(data) {
      mining_info = data;

      $.getJSON('/bitcoind/getpeerinfo', function(data) {
        bitcoind_peer_info = data;

        $(document).trigger('update_bitcoind');
      });
    });
  });
}

var block_probability, hashes_to_win, total_bitcoins, block_interval, block_eta;
var fetchBlockchainInfo = function() {
  $.getJSON('https://blockchain.info/q/probability?cors=true', function(data) {
    block_probability = parseFloat(data);

    $.getJSON('https://blockchain.info/q/hashestowin?cors=true', function(data) {
      hashes_to_win = data;

      $.getJSON('https://blockchain.info/q/totalbc?cors=true', function(data) {
        total_bitcoins = satoshiToBTC(data);

        $.getJSON('https://blockchain.info/q/interval?cors=true', function(data) {
          block_interval = data;

          $.getJSON('https://blockchain.info/q/eta?cors=true', function(data) {
            block_eta = data;

            $(document).trigger('update_blockchain_info');
          });
        });
      });
    });
  });
}

var fetchGraph= function(interval) {
  $.getJSON('/web/currency_info', function(currency_info) {
    change_period('hour', currency_info, true);
    $(document).trigger('update_time');
  });
};

var updateGraph = function() {
  $('title').text('Updating graph...');
  $('#updated').addClass('updating').text('Updating graph...');

  $(document).trigger('update_graph');
}

var updateLatency = function () {
  $.getJSON('/web/graph_data/getwork_latency/last_hour', function(data) {
    if (data) {
      $.map(data, function(row) {
        if (getwork_latency == null) {
          getwork_latency = row[1];
        }
      });
    }

    if (getwork_latency) {
      $('#node_latency')
        .text((getwork_latency * 1e3).toFixed(0).toString() + ' ms');
    } else {
      $('#node_latency').html('&dash;');
    }
  });
}

// update tables and miner data, hide any previous alerts

var updateData = function() {
  if(!$('#node_alerts').hasClass('hidden')) {
    $('#node_alerts').fadeOut(0, function() {
      $(this).attr('style', '').addClass('hidden');
    });
  }

  $('title').text('Updating data...');
  $('#updated').addClass('updating').text('Updating data...');
  $(document).trigger('update');
}

setInterval(updateData, config.reload_interval * 1000);
setInterval(updateGraph, config.reload_chart_interval * 1000);