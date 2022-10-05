#!/usr/bin/node

const args = process.argv[2];
const size = parseInt(args);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 1; i <= size; i++) {
    const row = [];
    for (let j = 1; j <= size; j++) {
      row.push('X');
    }
    console.log(row.join(''));
  }
}
