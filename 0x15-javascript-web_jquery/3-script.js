$(function () {
  const $header = $('header');

  $('div#red_header').on('click', (e) => {
    $header.addClass('red');
    e.preventDefault();
  });
});
