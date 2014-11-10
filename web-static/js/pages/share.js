function hex2a(hex) {
    var str = '';
    for (var i = 0; i < hex.length; i += 2) {
        var code = parseInt(hex.substr(i, 2), 16);
        str += code >= 32 && code <= 126 ? String.fromCharCode(code) : '?';
    }
    return str;
}

function target_to_difficulty(target) { return (0xffff0000 * Math.pow(2, 256-64) + 1)/(target + 1); }

var current_hash = null;
function reload(currency_info) {
    var share_hash = document.location.hash.substr(1);
    if(share_hash == current_hash) return;
    d3.json('../web/share/' + share_hash, function(share) {
        current_hash = share_hash;
        var b = d3.select('#share_data');
        b.selectAll('*').remove();
        var h1 = d3.select('#page-title');
            h1.text('');
            h1.append('a').attr('href', '.').text('P2Pool Node Status');
            h1.append('span').text(' > Share ' + share_hash.substr(-8));
        if(share == null) {
            b.append('p').text('share not found');
            return;
        }

        b.append('h2').text('Share data');

        var table = b.append('table').attr('class', 'table table-hover').append('tbody');
        tr = table.append('tr');
        tr.append('td').text('Parent');
        tr.append('td').attr('class','text-right').append('a').attr('href', '#' + share.parent).text(share.parent.substr(-8));
        tr.append('td').text('Children');
        tr.append('td').attr('class','text-right').selectAll().data(share.children).enter().append('span').text(' ').append('a')
                .attr('href', function(c){return '#' + c})
                .text(function(c){return c.substr(-8)});
        tr = table.append('tr');
        tr.append('td').text('Timestamp');
        tr.append('td').attr('class','text-right longDateFormat').text($.format.toBrowserTimeZone(new Date(1000*share.share_data.timestamp)));
        tr.append('td').text('Difficulty');
        tr.append('td').attr('class','text-right').text(target_to_difficulty(share.share_data.target));
        tr = table.append('tr');
        tr.append('td').text('Minimum difficulty');
        tr.append('td').attr('class','text-right').text(target_to_difficulty(share.share_data.max_target));
        tr.append('td').text('Payout address');
        tr.append('td').attr('class','text-right').append('code').text(share.share_data.payout_address);
        tr = table.append('tr');
        tr.append('td').text('Donation amount');
        tr.append('td').attr('class','text-right').text(d3.format('.3p')(share.share_data.donation));
        tr.append('td').text('Last stale');
        tr.append('td').attr('class','text-right').text(share.share_data.stale_info);
        tr = table.append('tr');
        tr.append('td').text('Nonce');
        tr.append('td').attr('class','text-right').text(share.share_data.nonce);
        tr.append('td').text('Desired version');
        tr.append('td').attr('class','text-right').text(share.share_data.desired_version);
        tr = table.append('tr');
        tr.append('td').text('Absolute height');
        tr.append('td').attr('class','text-right').text(share.share_data.absheight);
        tr.append('td').text('Absolute work');
        tr.append('td').attr('class','text-right').text(share.share_data.abswork);
        tr = table.append('tr');
        tr.append('td').text('Verified');
        tr.append('td').attr('class','text-right').text(share.local.verified);
        tr.append('td').text('Time first seen');
        tr.append('td').attr('class','text-right').text(new Date(1000*share.local.time_first_seen));
        if (share.local.peer_first_received_from) {
          tr = table.append('tr');
          tr.append('td').text('Received from');
          tr.append('td').attr('class','text-right').text(share.local.peer_first_received_from);
          tr.append('td');
          tr.append('td').attr('class','text-right');
        }

        b.append('h2').text('Block data');

        var table = b.append('table').attr('class', 'table table-hover').append('tbody');
        tr = table.append('tr');
        tr.append('td').text('Timestamp');
        tr.append('td').attr('class','text-right longDateFormat').text($.format.toBrowserTimeZone(new Date(1000*share.block.header.timestamp)));
        tr.append('td').text('Nonce');
        tr.append('td').attr('class', 'text-right').text(share.block.header.nonce);
        value = share.block.gentx.value;
        tr = table.append('tr');
        tr.append('td').text('Value');
        tr.append('td').attr('class','text-right').html('<button class="to_usd"><span data-value="'+value+'">' + value + ' ' + currency_info.symbol + '</span></button>');
        tr.append('td').text('Difficulty');
        tr.append('td').attr('class', 'text-right').text(target_to_difficulty(share.block.header.target));

        tr = table.append('tr');
        tr.append('td').text('Hash');
        tr.append('td').attr('class','text-right').attr('colspan', 3).text(share.block.hash);
        tr = table.append('tr');
        tr.append('td').text('Previous block');
        previous = tr.append('td').attr('class','text-right').attr('colspan', 3);
        previous.append('a').attr('href', 'block.html#' + share.block.header.previous_block).text(share.block.header.previous_block);
        tr = table.append('tr');
        tr.append('td').text('Merkle root');
        tr.append('td').attr('class','text-right').attr('colspan', 3).text(share.block.header.merkle_root);
        tr = table.append('tr');
        tr.append('td').text('Generation transaction hash');
        tr.append('td').attr('class','text-right').attr('colspan', 3).text(share.block.gentx.hash);

        bindCurrencyConversionButtons();
        return true;
    });
}

d3.json('../web/currency_info', function(currency_info) {
    reload(currency_info);
    setInterval(function(){ reload(currency_info) }, 100);
});