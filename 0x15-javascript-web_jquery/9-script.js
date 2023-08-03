$(function () {
  (async function () {
    const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
    const { hello } = await $.ajax({
      url,
      type: 'GET',
      cors: true,
      dataType: 'json',
      headers: {
        'Access-Control-Allow-Origin': '*'
      }
    });

    $('div#hello').text(hello);
  })();
});
