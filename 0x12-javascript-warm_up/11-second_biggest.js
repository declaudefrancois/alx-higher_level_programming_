#!/usr/bin/node
const arr = process.argv.slice(2)
  .map(v => parseInt(v))
  .sort((a, b) => b - a);

console.log(arr[1] ?? 0);
