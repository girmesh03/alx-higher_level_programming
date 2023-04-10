#!/usr/bin/node
// prints My number: <first argument converted in integer>
// if the first argument can be converted to an integer, and
// prints Not a number if the argument can't be converted to an integer

const myVar = process.argv[2];
if (isNaN(myVar)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(myVar));
}
