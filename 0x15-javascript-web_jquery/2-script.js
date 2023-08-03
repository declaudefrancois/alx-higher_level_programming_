$(function () {
  const $header = $('header');

  $('div#red_header').on('click', (e) => {
    $header.css('color', '#FF0000');
    e.preventDefault();
  });
});
