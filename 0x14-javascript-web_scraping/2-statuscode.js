#!/usr/bin/node
/**
 * display the status code of a GET request.
 */
const request = require('request');

const url = process.argv[2];
request(url, (error, res, body) => {
  if (error) { return; }

  if (res) {
    console.log('code: ' + res.statusCode);
  }
});
