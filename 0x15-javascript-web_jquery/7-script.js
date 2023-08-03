$(function () {
  (async function () {
    const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
    const { name } = await $.get(url);
    $('div#character').text(name);
  })();
});
