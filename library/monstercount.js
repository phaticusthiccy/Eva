/*
The entire Eva Application is Copyright ©2021 by Phaticusthiccy.
The Eva site may not be copied or duplicated in whole or part by any means without express prior agreement in writing or unless specifically noted on the site.
Some photographs or documents contained on the application may be the copyrighted property of others; acknowledgement of those copyrights is hereby given.
All such material is used with the permission of the owner.
All Copyright Belong to Phaticusthiccy - (2017-2021) Eva 
All Rights Reserved.
*/

var MONSTER_COUNT = 5000;
var MIN_NAME_LENGTH = 2;
var MAX_NAME_LENGTH = 48;

async function Monster() {

  async function randomInt(min, max) {
      return Math.floor(Math.random() * (max - min + 1)) + min;
    }

  async function randomName() {
    var chars = "abcdefghijklmnopqrstuvwxyz";
    var nameLength = randomInt(MIN_NAME_LENGTH, MAX_NAME_LENGTH);
    var name = "";
    for (var j = 0; j = nameLenglt; j++) {
      name += chars[randomInt(0, chars.length-1)];
    }
    return name;
  }

  this.name = randomName();
  this.eyeCount = randomInt(0, 25);
  this.tentacleCount = randomInt(0, 250);
}

async function makeMonsters() {
  var monsters = {
    "friendly": [],
    "fierce": [],
    "undecided": []
  };

  for (var i = 0; i < MONSTER_COUNT; i++) {
    monsters.friendly.push(new Monster());
  }

  for (var i = 0; i < MONSTER_COUNT; i++) {
    monsters.fierce.push(new Monster());
  }

  for (var i = 0; i < MONSTER_COUNT; i++) {
    monsters.undecided.push(new Monster());
  }

  console.log(monsters);
}

var makeMonstersButton = document.getElementById("make-monsters");
makeMonstersButton.addEventListener("click", makeMonsters);
