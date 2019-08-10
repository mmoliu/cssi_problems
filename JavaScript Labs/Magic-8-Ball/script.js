// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

const ball = document.querySelector('#ball');
const answer = document.querySelector('#answer');
const text = document.querySelector('#text');
const triangle = document.querySelector('triangle');

let positive = ["It is certain", "It is decidedly so", "Without a doubt buddy", "You may rely on it ", "As I see it", "Outlook good", "Signs point to yes"];
let negative = ["Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"];
let neutral = ["Reply hazy", "Try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate! Really concentrate! And ask again"];

function getRandomInt(max) {
  return Math.floor(Math.random() * Math.floor(max));
};

const generateAnswer = () => {
  let r = getRandomInt(2); //choose from positive negative neutral
  switch (r) {
    case 0:
      let rr = getRandomInt((positive.length-1));
      return positive[rr];
      break;
    case 1:
      let rrr = getRandomInt((negative.length-1));
      return negative[rrr];
      break;
    case 2:
      let rrrr = getRandomInt((neutral.length-1));
      return neutral[rrrr];
      break;
    default: return "No answer...";

  };
//use 2D array ot make more concise!!
};
ball.addEventListener('click', (e) => {
  answer.innerHTML = generateAnswer();

});
