#!/usr/bin/node
// prints the factorial of a number

function factorial (n) {
  if (isNaN(n) || n === 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

const number = process.argv[2];
console.log(factorial(parseInt(number)));
