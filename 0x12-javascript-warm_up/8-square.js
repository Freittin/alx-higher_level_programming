#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let height = 0; height < size; height++) {
    console.log('X'.repeat(size));
  }
}
