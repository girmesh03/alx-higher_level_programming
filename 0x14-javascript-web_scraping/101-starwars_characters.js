#!/usr/bin/node
// prints all characters of a Star Wars movie synchronously
const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// The request must be made to https://swapi-api.hbtn.io/api/films/:id
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;

// Make the request to get the movie data
request(url, (error, response, body) => {
  // if an error occurred during the request, print the error object
  if (error) {
    console.error(error);
    return;
  }

  // Parse movie data
  const movie = JSON.parse(body);

  // Get URLs of characters in the movie
  const charactersUrls = movie.characters;

  // Process each character URL
  const charactersPromises = charactersUrls.map(characterUrl => {
    // Return a new promise for each character URL
    return new Promise((resolve, reject) => {
      // Request the character URL
      request(characterUrl, (error, response, body) => {
        // If an error occurred during the request, reject the promise
        if (error) {
          reject(error);
          return;
        }

        // Parse character data
        const character = JSON.parse(body);

        // Resolve the promise with the character name
        resolve(character.name);
      });
    });
  });

  // Resolve all promises
  Promise.all(charactersPromises)
    .then(characters => {
      console.log(characters.join('\n'));
    })
    .catch(error => {
      console.error('Error:', error);
    });
});
