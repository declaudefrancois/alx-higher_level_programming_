#!/usr/bin/node
/**
 * prints all characters of a Star Wars movie.
 */
const request = require('request');

const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request(url, (error, res, body) => {
  if (error) { return; }

  if (res && res.statusCode === 200) {
    const movie = JSON.parse(body);
    movie.characters.forEach(url => {
      request(url, (error, res, body) => {
        if (error) { return; }

        if (res && res.statusCode === 200) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
