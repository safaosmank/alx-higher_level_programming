#!/usr/bin/node

const args = process.argv;

if (args.length <= 3) {
  console.log(0);
} else {
  let largest = parseInt(args[2]);
  let secondLargest = parseInt(args[3]);
  for (let i = 2; i < args.length; i++) {
    if (args[i] > largest) {
      largest = args[i];
    }
  }
  for (let j = 0; j < args.length; j++) {
    if (args[j] > secondLargest && args[j] < largest) {
      secondLargest = args[j];
    }
  }
  console.log(secondLargest);
}
