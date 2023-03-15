#!/usr/bin/node
const { readFileSync, writeFileSync } = require('fs');

const dataA = readFileSync(process.argv[2]);
const dataB = readFileSync(process.argv[3]);
writeFileSync(process.argv[4], dataA + dataB);
