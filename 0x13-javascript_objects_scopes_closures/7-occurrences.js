#!/usr/bin/node
module.exports.nbOccurences = function (list, searchElement) {
  return list.filter(e => e === searchElement).length;
};
