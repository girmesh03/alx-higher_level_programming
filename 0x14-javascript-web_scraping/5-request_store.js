#!/usr/bin/node
// Script that gets the contents of a webpage and stores it in a file.

// The first argument is the URL to request
const url = process.argv[2];

// The second argument the file path to store the body response
const filePath = process.argv[3];

// The request must be made and the body response must be written to the second argument
const request = require('request');

// Make the request and write the body response to the second argument
request(url, function (error, _response, body) {
  // If an error occurred during the request, print the error object
  if (error) {
    console.error(error);
  } else {
    const fs = require('fs');

    // Write the body response to the second argument
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      // If an error occurred during the writing, print the error object and return
      if (err) {
        console.log(err);
      }
    });
  }
});
