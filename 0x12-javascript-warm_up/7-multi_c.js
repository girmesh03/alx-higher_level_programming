#!/usr/bin/node
// prints x times C is fun
// if the first argument can't be converted to an integer, print
// Missing number of occurrences.

const myVar = process.argv[2];
if (isNaN(myVar)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(myVar); i++) {
    console.log('C is fun');
  }
}
