async function getHello (lang = 'fr') {
  const url = 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + lang;
  const { hello } = await $.ajax({
    url,
    type: 'GET',
    cors: true,
    dataType: 'json',
    headers: {
      'Access-Control-Allow-Origin': '*'
    }
  });

  return hello;
}

$(function () {
  const $hello = $('div#hello');
  const $btn = $('input#btn_translate');

  $btn.on('click', async (e) => {
    const lang = $('input#language_code').val();
    if (!lang) {
      // alert('Please enter a langage code !');
      return;
    }

    $btn.val('Loading...');
    $btn.attr('disabled', true);

    try {
      const hello = await getHello(lang);
      $hello.text(hello);
    } catch (e) {
      // alert('OOOOOOOOOOOH, try with another langage code !!!');
    } finally {
      $btn.val('Translate');
      $btn.attr('disabled', false);
    }

    e.preventDefault();
  });
});
