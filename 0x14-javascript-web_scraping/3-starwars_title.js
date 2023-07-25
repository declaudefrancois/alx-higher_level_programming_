#!/usr/bin/node
/**
 *  Prints the title of a Star Wars movie where
 *  the episode number matches the given arguments.
 */
const request = require('request');

const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request(url, (error, res, body) => {
  if (error) { return; }

  if (res && res.statusCode === 200) {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});
