#!/usr/bin/node
const n = parseInt(process.argv[2]);
function factorial (x) {
  if (isNaN(x) || x === 1) {
    return (1);
  } else {
    return (x * factorial(x - 1));
  }
}
