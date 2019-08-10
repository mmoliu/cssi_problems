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

console.log("Running Click Events Script");
const box1 = document.querySelector('#box1');
const box2 = document.querySelector('#box2');
const box3 = document.querySelector('#box3');
const box4 = document.querySelector('#box4');
const box5 = document.querySelector('#box5');
//const boxes = [box1, box2, box3];
const clicked =(b)=> {
  b.addEventListener('click', () => {
    if (b===box1) {
      box2.style.backgroundColor = 'red';
      box3.style.backgroundColor = 'red';
    }
    else if (b===box2) {
      box3.style.backgroundColor = 'pink';
      box1.style.backgroundColor = 'pink';
    }
    else if (b===box3) {
      box1.style.backgroundColor = 'orange';
      box2.style.backgroundColor = 'orange';
    };
    // switch (b) {
    //   case box1:
    //     box2.style.backgroundColor = b.style.backgroundColor;
    //     box3.style.backgroundColor = b.style.backgroundColor;
    //
    //     break;
    //   case box2:
    //     box3.style.backgroundColor = def;
    //     box1.style.backgroundColor = def;
    //   break;
    //   case box3:
    //     box1.style.backgroundColor = def;
    //     box2.style.backgroundColor = def;
    //   break;
    //   default: break;
    //
    // };

  });
};
clicked(box1);
clicked(box2);
clicked(box3);

const togg = (b) => {
  b.addEventListener('click', () => {
    if (b["className"] == "box active") {
      b.classList.remove("active");
    }
    else {
      b.classList.add("active");
    };
  });
};


togg(box4);
togg(box5);
