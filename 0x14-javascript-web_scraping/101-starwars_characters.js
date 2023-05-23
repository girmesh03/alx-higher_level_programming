#!/usr/bin/node
// prints all characters of a Star Wars movie synchronously
const request = require('request');

// Get movie ID from command line argument
const movieId = process.argv[2];

// Construct URL to fetch movie data
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a request to fetch movie data
request(url, (error, response, body) => {
  // Handle errors
  if (error) {
    console.error(error);
    return;
  }

  // Parse JSON string into object
  const movie = JSON.parse(body);

  // Get characters from movie object
  const characters = movie.characters;

  // Create an array of Promises that will be resolved when each character is fetched
  const characterPromises = characters.map(character => {
    return new Promise((resolve, reject) => {
      request(character, (error, response, body) => {
        // Handle errors
        if (error) {
          reject(error);
        } else {
          // Resolve with character name
          resolve(JSON.parse(body).name);
        }
      });
    });
  });

  // Resolve all Promises
  Promise.all(characterPromises)
    .then(characters => {
      console.log(characters.join('\n'));
    })
    .catch(error => {
      console.error(error);
    });
});

