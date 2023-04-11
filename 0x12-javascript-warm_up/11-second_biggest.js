#!/usr/bin/node
// A script that searches the second biggest integer in the list of arguments.

const args = process.argv.slice(2);
if (args.length <= 1) {
  console.log(0);
} else {
  const sorted = args.sort((a, b) => a - b);
  console.log(sorted[sorted.length - 2]);
}
