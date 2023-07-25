#!/usr/bin/node
/**
 * gets the contents of a webpage and stores it in a file.
 */
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];
request
  .get(url)
  .on('error', (error) => { console.log(error); })
  .pipe(fs.createWriteStream(filePath));
