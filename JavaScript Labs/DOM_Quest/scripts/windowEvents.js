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

console.log("Running Window Events Script");
const box6 = document.querySelector("#box6");
const box7 = document.querySelector("#rect");
const header = document.querySelector("#yot");

window.addEventListener("keypress", (e) => {
  console.log(e.keyCode);
  box6.style.borderRadius = "50%"; //how to make perfect circle?
  box6.style.width = "50px";
  box6.style.width = "50px";
});

window.onscroll = function() {myFunction()};

function myFunction() {
  if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
      box7.style.backgroundColor = "black";
      header.innerHTML = "Congrats! I'm proud of u!!";
      console.log("It's working!");
  }
  else {
    box7.style.backgroundColor = "tomato";
    header.innerHTML = "";
  };
}
