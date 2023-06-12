#!/usr/bin/node
function factorial (n) {
  if (n === 1 || n === 0) { return 1; }

  return n * factorial(n - 1);
}

const nbr = parseInt(process.argv[2]);
if (isNaN(nbr)) {
  console.log(1);
} else {
  console.log(factorial(nbr));
}
