#!/usr/bin/node
const c = parseInt(process.argv[2]);
if (isNaN(c)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < c; i++) {
    console.log('X'.repeat(c));
  }
}
