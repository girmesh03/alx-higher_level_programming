#!/usr/bin/node
// prints a square

const myVar = process.argv[2];
if (isNaN(myVar)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(myVar); i++) {
    console.log('X'.repeat(parseInt(myVar)));
  }
}
