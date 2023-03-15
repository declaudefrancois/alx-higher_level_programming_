#!/usr/bin/node
let count = 0;
module.exports.logMe = function (item) {
  console.log(`${count}:`, item);
  count++;
};
