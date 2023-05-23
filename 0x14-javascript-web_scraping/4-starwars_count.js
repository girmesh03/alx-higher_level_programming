#!/usr/bin/node
// Script that prints the number of movies where the character “Wedge Antilles” is present.

// The first argument is the API URL of the Star wars API: https://swapi-api.hbtn.io/api/films/
const apiUrl = process.argv[2];

// The request must be made to this URL with the character ID 18
const request = require('request');

// Make the request and print the number of movies where the character “Wedge Antilles” is present
request(apiUrl, function (error, _response, body) {
  // If an error occurred during the request, print the error object
  if (error) {
    console.error(error);
  } else {
    // otherwise, print the number of movies where the character “Wedge Antilles” is present
    const movies = JSON.parse(body).results;
    let count = 0;
    for (const movie of movies) {
      for (const character of movie.characters) {
        if (character.endsWith('/18/')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
