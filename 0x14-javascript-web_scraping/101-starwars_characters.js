#!/usr/bin/node
// prints all characters of a Star Wars movie synchronously
const request = require('request');

// Get movie ID from command line argument
const movieId = process.argv[2];

// Construct URL to fetch movie data
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a request to fetch movie data
request(url, (error, response, body) => {
  // If an error occurred during the request, print the error object
  if (error) {
    console.error('Error:', error);
    return;
  }

  // Parse JSON string into object
  const movie = JSON.parse(body);

  // Get characters from movie object
  const charactersUrls = movie.characters;

  // Create an array of Promises that will be resolved when each character is fetched
  const charactersPromises = charactersUrls.map(characterUrl => {
    // Create a Promise that will be resolved when the character is fetched
    return new Promise((resolve, reject) => {
      request(characterUrl, (error, response, body) => {
        // if an error occurred, reject the Promise
        if (error) {
          reject(error);
          return;
        }

        // Resolve with character name
        const character = JSON.parse(body)
        resolve(character.name);

      });
    });
  });

  // Resolve all Promises
  Promise.all(charactersPromises)
    .then(characters => {
      console.log(characters.join('\n'));
    })
    .catch(error => {
      console.error('Error:', error);
    });
});

