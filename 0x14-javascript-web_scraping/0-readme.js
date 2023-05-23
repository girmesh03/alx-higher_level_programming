#!/usr/bin/node
// Write a script that reads and prints the content of a file.
const fs = require('fs');

// The content of the file must be read in utf-8
const file = process.argv[2];

// Read the file and print its content
fs.readFile(file, 'utf-8', (err, data) => {
  // If an error occurred during the reading, print the error object and return
  if (err) {
    console.error(err);
    return;
  }
  // otherwise, print the content of the file
  console.log(data);
});
