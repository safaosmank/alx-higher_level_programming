#!/usr/bin/node

const args = process.argv;
const count = args[2];

if (typeof count === 'undefined') {
  console.log('Missing number of occurrences');
} else {
  for (let i = 1; i <= count; i++) {
    console.log('C is fun');
  }
}
