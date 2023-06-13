#!/usr/bin/node
module.exports.esrever = function (list) {
  const listLen = list.length;
  const reversedList = new Array(listLen);

  for (let i = 0; i < listLen; i++) {
    reversedList[i] = list[listLen - 1 - i];
    reversedList[listLen - 1 - i] = list[i];
  }

  return reversedList;
};
