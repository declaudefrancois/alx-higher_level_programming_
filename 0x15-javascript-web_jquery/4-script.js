$(function () {
  const $header = $('header');

  $('div#toggle_header').on('click', (e) => {
    $header.toggleClass('green');
    $header.toggleClass('red');
    e.preventDefault();
  });
});
