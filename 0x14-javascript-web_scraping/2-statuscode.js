#!/usr/bin/node
// A script that display the status code of a GET request.

// The first argument is the URL to request (GET)
const url = process.argv[2];

// The request must be made and the status code must be printed.
const request = require('request');

// Make the request and print the status code
request(url, function (error, response) {
  // If an error occurred during the request, print the error object
  if (error) {
    console.error(error);
  } else {
    // otherwise, print the status code
    console.log('code: ' + response.statusCode);
  }
});
