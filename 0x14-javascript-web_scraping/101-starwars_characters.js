#!/usr/bin/node

// A script that prints all characters of a Star Wars movie:

// The first argument is the Movie ID - example: 3 = “Return of the Jedi”
const movieId = process.argv[2];

// The request must be made to https://swapi.dev/api/films/:id
const url = `https://swapi.dev/api/films/${movieId}`;

// Display one character name by line in the same order of the list “characters” in the /films/ response
const request = require('request');

function getCharacterName(url) {
  return new Promise((resolve, reject) => {
    request(url, function (error, _response, body) {
      if (error) {
        reject(error);
      } else {
        const characterName = JSON.parse(body).name;
        resolve(characterName);
      }
    });
  });
}

request(url, function (error, _response, body) {
  if (error) {
    console.error(error);
  } else {
    const characters = JSON.parse(body).characters;
    const characterPromises = characters.map(getCharacterName);

    Promise.all(characterPromises)
      .then((characterNames) => {
        for (const characterName of characterNames) {
          console.log(characterName);
        }
      })
      .catch((error) => {
        console.error(error);
      });
  }
});
