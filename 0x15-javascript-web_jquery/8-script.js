$(function () {
  (async function () {
    const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
    const { results: movies } = await $.get(url);

    const $movies = $('ul#list_movies');
    movies.forEach((movie) => {
      $movies.append(
       `<li>
         <h1>${movie.title} (Episode ${movie.episode_id})</h1>
         <p>${movie.opening_crawl}</p>
         <p><strong>Director: </strong>${movie.director}</p>
         <p><strong>Producer: </strong>${movie.producer}</p>
         <p><strong>Realeased: </strong>${movie.release_date}</p>
       </li>`);
    });
  })();
});
