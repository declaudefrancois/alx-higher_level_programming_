$(function () {
  const $ul = $('ul.my_list');

  $('div#add_item').on('click', (e) => {
    $ul.append('<li>Item</li>');
    e.preventDefault();
  });

  $('div#remove_item').on('click', (e) => {
    $ul.find('li').last()?.remove();
    e.preventDefault();
  });

  $('div#clear_list').on('click', (e) => {
    $ul.find('li').remove();
    e.preventDefault();
  });
});
