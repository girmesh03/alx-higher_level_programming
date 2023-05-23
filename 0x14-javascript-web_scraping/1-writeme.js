#!/usr/bin/node

// Write a script that writes a string to a file.
const fs = require('fs');

// The first argument is the file path
const file = process.argv[2];

// The second argument is the string to write
const string = process.argv[3];

// Write the string to the file
fs.writeFile(file, string, 'utf-8', (err) => {
  // If an error occurred during the writing, print the error object and return
  if (err) {
    console.log(err);
  }
});
