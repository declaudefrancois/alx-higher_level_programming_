$(function () {
  const $header = $('header');

  $('div#update_header').on('click', (e) => {
    $header.text('New Header!!!');
    e.preventDefault();
  });
});
