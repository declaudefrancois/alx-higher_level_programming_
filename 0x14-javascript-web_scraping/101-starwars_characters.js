#!/usr/bin/node
/**
 * prints all characters of a Star Wars movie.
 */
const request = require('request');

const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;
request(url, async (error, res, body) => {
  if (error) { return; }

  if (res && res.statusCode === 200) {
    const movie = JSON.parse(body);
    const names = await Promise.all(movie.characters.map(url => getCharacterName(url)));
    console.log(names.join('\n'));
  }
});

/**
 * Get Character name by its url ressource.
 */
function getCharacterName (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, res, body) => {
      if (error) { reject(error); }

      if (res && res.statusCode === 200) {
        resolve(JSON.parse(body).name);
      }
    });
  });
}
