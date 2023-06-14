#!/usr/bin/node
const data = require('./101-data').dict;
const userIds = {};

for (const key in data) {
  if (!userIds[data[key]]) userIds[data[key]] = [];

  userIds[data[key]].push(key);
}

console.log(userIds);
