#!/usr/bin/node

const request = require('request');

function getCharacters (movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;
  request(url, (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      const film = JSON.parse(body);
      const characterUrls = film.characters;
      characterUrls.forEach((characterUrl) => {
        request(characterUrl, (err, res, charBody) => {
          if (err) {
            console.error(err);
          } else {
            const character = JSON.parse(charBody);
            console.log(character.name);
          }
        });
      });
    }
  });
}
if (require.main === module) {
  const movieId = process.argv[2];
  getCharacters(movieId);
}
