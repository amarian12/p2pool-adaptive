var donation_address = "";

$(document).ready(function() {
  $(document).trigger('init');

  // load header/footer
  if(config.header_url && config.header_url.length > 0) {
    $("#header").load(config.header_url);
  }
  if(config.footer_url && config.footer_url.length > 0) {
    $("#footer").load(config.footer_url);
  }

  // set node name
  if (config.node_name) {
    $('#node').removeClass('hidden').text(config.node_name);
    $('#_node').removeClass('hidden');
  }

  // create donation address link
  if(config.donation_address && config.donation_address.length > 0) {
    donation_address = config.donation_address;
  }

  // get the latest bitcoin price
  var dollar_per_bitcoin;
  if (config.convert_bitcoin_to_usd) {
    getLatestBitcoinPrice();
    bindCurrencyConversionButtons();
  } else {
    $('button.to_usd').attr('disabled', true);
  }

  // set updated at
  var dts = $.format.date(new Date(), 'yyyy-MM-dd HH:mm:ss');
  $('#updated').text('Updated: ' + dts);

  rotateAd();
});