#!/usr/bin/node
const nbr = parseInt(process.argv[2]);
if (isNaN(nbr)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < nbr; i++) {
    console.log('X'.repeat(nbr));
  }
}
