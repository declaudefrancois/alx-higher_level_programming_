#!/usr/bin/node
module.exports.esrever = function (list) {
  return Object.keys(list)
    .sort((a, b) => b - a)
    .map(v => list[v]);
};
