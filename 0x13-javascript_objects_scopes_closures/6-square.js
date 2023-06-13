#!/usr/bin/node
const _Square = require('./5-square');

class Square extends _Square {
  charPrint (c) {
    const unit = c ?? 'X';
    for (let i = 0; i < this.width; i++) {
      console.log(unit.repeat(this.width));
    }
  }
}

module.exports = Square;
