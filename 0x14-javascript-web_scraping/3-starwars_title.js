#!/usr/bin/node
// A script that prints the title of a Star Wars movie where the episode number matches a given integer.

// The first argument is the episode number
const episodeNumber = process.argv[2];

// The request must be made to the Star Wars API with the episode number
const request = require('request');

// Make the request and print the title of the movie
request('https://swapi-api.hbtn.io/api/films/' + episodeNumber, function (error, _response, body) {
  // If an error occurred during the request, print the error object
  if (error) {
    console.error(error);
  } else {
    // otherwise, print the title of the movie
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});
