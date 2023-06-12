#!/usr/bin/node
const nums = process.argv
  .slice(2)
  .sort((a, b) => b - a);

console.log(nums[1] ?? 0);
