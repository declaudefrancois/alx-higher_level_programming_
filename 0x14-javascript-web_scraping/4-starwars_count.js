#!/usr/bin/node
/**
 * Prints the number of movies where the
 * character “Wedge Antilles” is present.
 */
const request = require('request');

const url = process.argv[2];
const wedgeRessource = url.split('films')[0] + 'people/18/';
request(url, (error, res, body) => {
  if (error) { return; }

  if (res && res.statusCode === 200) {
    const movies = JSON.parse(body);
    const wedgeMovies = movies.results.filter(
      (movie) => movie.characters.indexOf(wedgeRessource) !== -1
    );
    console.log(wedgeMovies.length);
  }
});
