var current_hash = null;
var miner_hash = document.location.hash.substr(1);
var currency_info;
var local_stats, current_payouts;

var h1 = d3.select('#page-title');
    h1.append('a').attr('href', '.').text('P2Pool Node Status');
    h1.append('span').text(' > Miner ' + miner_hash.substr(0,8));

periods = ["Hour", "Day", "Week", "Month", "Year"];
d3.select("#period_chooser").selectAll().data(periods).enter().append("a")
    .text(function(period) { return period })
    .attr('href', function(period){ return "?" + period + "#" + miner_hash})
    .attr("style", function(d, i) { return (i == 0 ? "" : "margin-left:.4em;")});

var period = window.location.search.substr(1);

if(period.length < 3) {
    window.location.hash = miner_hash;
    window.location.search = "Hour";
} else if (miner_hash == "") {
    window.location = '/';
} else {
    d3.json('../web/currency_info', function(currency_info_response) {
        currency_info = currency_info_response;
    });

    $.getJSON('/local_stats', function(data) {
      if(data) {
        local_stats = data;

        $.getJSON('/current_payouts', function(data) {
          if(data) {
            current_payouts = data;

            loadStats();
          }
        });
      }
    });

    loadGraphs();
    loadMinerTransactions();
    loadRecentShares();
}

function loadStats() {
  d3.select('#address').text(miner_hash);

  hashrate = local_stats.miner_hash_rates[miner_hash];
  doa = local_stats.miner_dead_hash_rates[miner_hash] || 0;
  doa_prop = (parseFloat(doa) / parseFloat(hashrate)) * 100;
  payout = current_payouts[miner_hash] || 0;

  d3.select('#hashrate').text(formatHashrate(hashrate));
  d3.select('#doa').text(formatHashrate(doa));
  d3.select('#doa_prop').text(doa_prop.toFixed(2) + '%');

  if (payout) {
    $('#payout').attr('data-value', payout);
    d3.select('#payout').text(parseFloat(payout).toFixed(8).toString() + ' ' + currency_info.symbol);
  }
  else {
    d3.select('#payout').text('no shares yet');
  }
}

function loadGraphs() {
    var lowerperiod = period.toLowerCase();

    d3.select("#period_current").text(period);

    d3.json("../web/graph_data/miner_hash_rates/last_" + lowerperiod, function(data) {
        d3.json("../web/graph_data/miner_dead_hash_rates/last_" + lowerperiod, function(dead_data) {
            d3.json("../web/graph_data/current_payouts/last_" + lowerperiod, function(current_payouts) {
                d3.select("#loading").selectAll("*").remove();

                var div = d3.select('#local_rate_graph').selectAll().data([miner_hash]).enter().append("div");
                div.append('h3').text('Local Hashrate');
                div.append("svg:svg").each(function(u) {
                    plot(d3.select(this), "H/s", "H", [
                        {"data": data.map(function(d){ return [d[0], u in d[1] ? d[1][u] : d[3], d[2]] }), "color": "#5bb75b", "label": "Total"},
                        {"data": dead_data.map(function(d){ return [d[0], u in d[1] ? d[1][u] : d[3], d[2]] }), "color": "#FF0000", "label": "Dead"}
                    ]);
                });


                var div = d3.select('#payout_graph').selectAll().data([miner_hash]).enter().append("div");
                div.append('h3').text('Payout');
                div.append("svg:svg").each(function(u) {
                    plot(d3.select(this), currency_info.symbol, null, [
                        {"data": current_payouts.map(function(d){ return [d[0], u in d[1] ? d[1][u] : d[3], d[2]] }), "color": "#5bb75b"}
                    ]);
                });
            });
        });
    });
}

function loadMinerTransactions() {
  $.getJSON('https://blockchain.info/q/getreceivedbyaddress/' + miner_hash + '?cors=true', function(data) {
    var received_by_address = data;

    $.getJSON('https://blockchain.info/q/getsentbyaddress/' + miner_hash + '?cors=true', function(data) {
      var sent_by_address = data;

      $.getJSON('https://blockchain.info/q/addressbalance/' + miner_hash + '?cors=true', function(data) {
        var address_balance = data;

        $('#total_received')
          .attr('data-value', satoshiToBTC(received_by_address))
          .text(satoshiToBTC(received_by_address).toString() + ' BTC');

        $('#total_sent')
          .attr('data-value', satoshiToBTC(sent_by_address))
          .text(satoshiToBTC(sent_by_address).toString() + ' BTC');

        $('#current_balance')
          .attr('data-value', satoshiToBTC(address_balance))
          .text(parseFloat(satoshiToBTC(address_balance)).toString() + ' BTC');
      });
    });
  });
}

function loadRecentShares() {
  $.getJSON('/web/my_share_hashes', function(data) {
    recent_shares = data;

    $.each(recent_shares, function(key, share_hash) {
      var shareinfo;
      $.ajax('/web/share/' + share_hash, {
          async: false,
          success: function(data) {
              if (data) {
                  shareinfo = data['share_data'];
              }
          }
      });

      if (!shareinfo) { return; }

      if (shareinfo['payout_address'] != miner_hash) {
        return;
      } else {
        var blockinfo= $('<a/>').attr('href', 'share.html#' + share_hash).text(share_hash);
        var stale_info = $('<span/>');
        if (shareinfo.stale_info == null) {
          stale_info.addClass('green').text('valid');
        } else {
          stale_info.addClass('red').text(shareinfo.stale_info);
        }

        tr= $('<tr/>').attr('id', share_hash);
        tr.append($('<td class="hidden"/>').text(shareinfo.timestamp));
        tr.append($('<td/>').text($.format.prettyDate(new Date(shareinfo.timestamp * 1000))));
        tr.append($('<td/>').append(blockinfo));
        tr.append($('<td/>').addClass('text-center').append(stale_info));
        $('#recent_shares tbody').append(tr);

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
      }
    });
  });
}