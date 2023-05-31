#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(url, async (error, response, body) => {
  error && console.log(error);

  const charactersArray = (JSON.parse(response.body).characters);
  for (const character of charactersArray) {
    await new Promise((resolve, reject) => {
      request(character, (error, response, body) => {
        error && console.log(error);

        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
