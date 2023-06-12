#!/usr/bin/node
const argvLen = process.argv.length;
const msg = argvLen === 2
  ? 'No argument'
  : argvLen === 3
    ? 'Argument found'
    : 'Arguments found';

console.log(msg);
