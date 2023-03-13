#!/usr/bin/node
const msg = process.argv.length === 2
  ? 'No argument'
  : process.argv.length === 3
    ? 'Argument found'
    : 'Arguments found';

console.log(msg);
