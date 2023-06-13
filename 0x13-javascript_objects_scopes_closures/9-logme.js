#!/usr/bin/node
let callsCount = 0;

module.exports.logMe = function (item) {
  console.log(`${callsCount}: ${item}`);
  callsCount++;
};
