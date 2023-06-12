#!/usr/bin/node
const nbr = parseInt(process.argv[2]);
if (!isNaN(nbr)) {
  console.log('My number: ' + nbr);
} else {
  console.log('Not a number');
}
