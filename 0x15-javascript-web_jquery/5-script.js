$(function () {
  const $ul = $('ul.my_list');

  $('div#add_item').on('click', (e) => {
    $ul.append('<li>Item</li>');
    e.preventDefault();
  });
});
