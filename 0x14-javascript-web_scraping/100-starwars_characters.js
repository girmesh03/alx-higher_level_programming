#!/usr/bin/node
// Script that prints all characters of a Star Wars movie:

// The first argument is the Movie ID - example: 3 = “Return of the Jedi”
const movieId = process.argv[2];

// The request must be made to https://swapi-api.hbtn.io/api/films/:id
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;

// Display one character name by line in the same order of the list “characters” in the /films/ response
const request = require('request');
request(url, function (error, _response, body) {
  if (error) {
    console.error(error);
  } else {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      request(character, function (error, _response, body) {
        if (error) {
          console.error(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
