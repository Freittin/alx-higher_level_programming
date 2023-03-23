#!/usr/bin/node
const n = process.argv[2];
if (isNaN(n)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < n; i++) {
    console.log('C is fun');
  }
}
