var current_hash = null;
function reload(currency_info) {
    var block_hash = document.location.hash.substr(1);
    if(block_hash == current_hash) return;
    d3.json('../bitcoind/block/' + block_hash, function(block) {
        current_hash = block_hash;
        var b = d3.select('#block_data');
        b.selectAll('*').remove();
        var h1 = d3.select('#page-title');
            h1.text('');
            h1.append('a').attr('href', '.').text('P2Pool Node Status');
            h1.append('span').text(' > Block ' + block_hash.substr(-8));
        if (block == null) {
            b.append('p').text('block not found');
            return;
        }

        var table = b.append('table').attr('class', 'table table-hover').append('tbody');
        tr = table.append('tr');
        tr.append('td').text('Timestamp');
        tr.append('td').attr('class','text-right longDateFormat').text($.format.toBrowserTimeZone(new Date(1000*block.time)));
        tr.append('td').text('Difficulty');
        tr.append('td').attr('class', 'text-right').text(block.difficulty);
        tr = table.append('tr');
        tr.append('td').text('Confirmations');
        tr.append('td').attr('class','text-right').text(block.confirmations);
        tr.append('td').text('Height');
        tr.append('td').attr('class', 'text-right').text(block.height);

        tr = table.append('tr');
        tr.append('td').text('Hash');
        tr.append('td').attr('class','text-right').attr('colspan', 3).text(block.hash);
        tr = table.append('tr');
        tr.append('td').text('Previous block');
        tr.append('td').attr('class','text-right').attr('colspan', 3).append('a').attr('href', '#' + block.previousblockhash).text(block.previousblockhash);
        tr = table.append('tr');
        tr.append('td').text('Next block');
        tr.append('td').attr('class','text-right').attr('colspan', 3).append('a').attr('href', '#' + block.nextblockhash).text(block.nextblockhash);
        tr = table.append('tr');
        tr.append('td').text('Merkle root');
        tr.append('td').attr('class','text-right').attr('colspan', 3).text(block.merkleroot);
        
        b.append('p').append('h3').text('Transactions');
        var transactions = b.append('ul');
        $.each(block.tx, function(index, value) {
            transactions.append('li').append('a').attr('href', 'transaction.html#' + value).text(value);
        });
        return true;
    });
}

d3.json('../web/currency_info', function(currency_info) {
    reload(currency_info);
    setInterval(function(){ reload(currency_info) }, 100);
});