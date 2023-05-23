#!/usr/bin/node
// A script that prints all characters of a Star Wars movie synchronously

// Require the request module
const request = require('request');

// Get movie ID from command line argument
const movieId = process.argv[2];

// Construct URL to fetch movie data
const url = `https://swapi.dev/api/films/${movieId}`;

// Make a request to fetch movie data
request(url, (error, response, body) => {
  // Handle errors
  if (error) {
    console.error('Error:', error);
    return;
  }

  // Parse movie data
  const film = JSON.parse(body);

  // Get URLs of characters in the movie
  const charactersUrls = film.characters;

  // Fetch and print the character names synchronously
  fetchAndPrintCharacters(charactersUrls);
});

function fetchAndPrintCharacters(urls) {
  if (urls.length === 0) {
    return;
  }

  const characterUrl = urls.shift();

  // Make a request to fetch character data
  request(characterUrl, (error, response, body) => {
    // Handle errors
    if (error) {
      console.error('Error:', error);
      return;
    }

    // Parse character data
    const character = JSON.parse(body);

    // Print the name of the character
    console.log(character.name);

    // Fetch and print the next character name
    fetchAndPrintCharacters(urls);
  });
}
