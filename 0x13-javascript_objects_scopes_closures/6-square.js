#!/usr/bin/node
const _Square = require('./5-square.js');

class Square extends _Square {
  charPrint (c) {
    if (typeof c !== 'undefined') {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.width));
      }
      return;
    }
    super.print();
  }
}

module.exports = Square;
