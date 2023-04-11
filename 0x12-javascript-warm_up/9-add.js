#!/usr/bin/node
// prints the addition of 2 integers

const firstNumber = process.argv[2];
const secondNumber = process.argv[3];
if (isNaN(firstNumber) || isNaN(secondNumber)) {
  console.log('NaN');
} else {
  console.log(parseInt(firstNumber) + parseInt(secondNumber));
}
