#!/usr/bin/node
module.exports.nbOccurences = function (list, searchElement) {
  let occurences = 0;
  const listLenght = list.length;

  for (let i = 0; i < listLenght; i++) {
    if (list[i] === searchElement) { occurences++; }
  }

  return occurences;
};
