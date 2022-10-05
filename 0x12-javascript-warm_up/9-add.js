#!/usr/bin/node

const args = process.argv;

function add (a, b) {
  a = parseInt(args[2]);
  b = parseInt(args[3]);
  console.log(a + b);
}
add(args[2], args[3]);
