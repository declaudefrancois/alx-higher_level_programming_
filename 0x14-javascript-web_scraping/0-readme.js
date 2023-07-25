#!/usr/bin/node
/**
 * Reads and prints the content of a file.
 */
const fs = require('fs');
const filePath = process.argv[2];

fs.readFile(filePath, 'utf8', (error, content) => {
  if (error) {
    console.log({ error });
    return;
  }

  console.log(content);
});
