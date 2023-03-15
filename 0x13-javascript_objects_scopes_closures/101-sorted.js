#!/usr/bin/node
const dict = require('./101-data.js').dict;
const arr = [];

for (const a in dict) {
  arr.push([dict[a], a]);
}

const dictSorted = arr
  .sort((a, b) => a[0] - b[0])
  .reduce((acc, curr) => {
    if (!Array.isArray(acc[curr[0]])) { acc[curr[0]] = []; }

    acc[curr[0]].push(curr[1]);
    return acc;
  }, {});

console.log(dictSorted);
