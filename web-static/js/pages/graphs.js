d3.json('../local_stats', function(local_stats) {
    d3.select('#warnings').selectAll().data(local_stats.warnings).enter().append('p')
        .text(function(w){ return 'Warning: ' + w })
        .attr('style', 'color:red;border:1px solid red;padding:5px');
})

periods = ["Hour", "Day", "Week", "Month", "Year"];
d3.select("#period_chooser").selectAll().data(periods).enter().append("a")
    .text(function(period) { return period })
    .attr('href', function(period){ return "?" + period })
    .attr("style", function(d, i) { return (i == 0 ? "" : "margin-left:.4em;") });
period = window.location.search.substr(1);
if(period.length < 3) {
    window.location.search = "Day";
} else {
    d3.json('../web/currency_info', function(currency_info) {
        change_period(period, currency_info);
    });
}
$('#period').text(period);
