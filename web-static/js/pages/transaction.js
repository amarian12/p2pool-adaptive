var current_hash = null;
function reload(currency_info) {
    var transaction_hash = document.location.hash.substr(1);
    if(transaction_hash == current_hash) return;
    d3.json('../bitcoind/rawtransaction/' + transaction_hash, function(transaction) {
        current_hash = transaction_hash;
        var b = d3.select('#transaction_data');
        b.selectAll('*').remove();
        var h1 = d3.select('#page-title');
            h1.text('');
            h1.append('a').attr('href', '.').text('P2Pool Node Status');
            h1.append('span').text(' > Transaction ' + transaction_hash.substr(-8));
        if (transaction == null) {
            b.append('p').text('transaction not found');
            return;
        }

        var transaction_total = 0;
        var transaction_count = 0;
        $.each(transaction.vout, function(index, vout) {
            transaction_count += 1;
            transaction_total += vout.value;
        });
        average_transaction = (transaction_total / transaction_count).toFixed(8);

        var table = b.append('table').attr('class', 'table table-hover').append('tbody');
        tr = table.append('tr');
        tr.append('td').text('Timestamp');
        tr.append('td').attr('class','text-right longDateFormat').text($.format.toBrowserTimeZone(new Date(1000*transaction.time)));
        tr.append('td').text('Confirmations');
        tr.append('td').attr('class', 'text-right').text(transaction.confirmations);
        tr = table.append('tr');
        tr.append('td').text('Block value');
        tr.append('td').attr('class','text-right').html('<button class="to_usd"><span data-value="'+transaction_total+'">' + transaction_total + ' ' + currency_info.symbol + '</span></button>');
        tr.append('td').text('Average transaction');
        tr.append('td').attr('class', 'text-right').html('<button class="to_usd"><span data-value="'+average_transaction+'">' + average_transaction + ' ' + currency_info.symbol + '</span></button>');

        tr = table.append('tr');
        tr.append('td').text('Hash');
        tr.append('td').attr('class','text-right').attr('colspan', 3).text(transaction.txid);
        tr = table.append('tr');
        tr.append('td').text('Block');
        tr.append('td').attr('class', 'text-right').attr('colspan', 3).append('a').attr('href', 'block.html#' + transaction.blockhash).text(transaction.blockhash);

        var address_table = b.append('table').attr('class', 'table table-hover').attr('id', 'transaction_table');
        var head = address_table.append('thead').append('tr');
        head.append('th').text('Address');
        head.append('th').attr('class', 'text-right').text('Value');
        address_table = address_table.append('tbody');

        $.each(transaction.vout, function(index, vout) {
            if (vout.value <= 0) { 
                return; 
            }

            var tr = address_table.append('tr');
            tr.append('td').append('a').attr('href', currency_info.address_explorer_url_prefix + vout.scriptPubKey.addresses).text(vout.scriptPubKey.addresses);

            tr.append('td').attr('class', 'text-right').html('<button class="to_usd"><span data-value="'+vout.value+'">' + vout.value + ' ' + currency_info.symbol + '</span></button>');
        });

        bindCurrencyConversionButtons();
        return true;
    });
}

d3.json('../web/currency_info', function(currency_info) {
    reload(currency_info);
    setInterval(function(){ reload(currency_info) }, 100);
});