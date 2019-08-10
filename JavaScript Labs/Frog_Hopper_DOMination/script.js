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

let currentlily = 1;

const frogger = document.querySelector('#frog');/* Use a querySelector to grab your frog from your HTML */;
const lilypad1 = document.querySelector('#lilypad1');
const lilypad2 = document.querySelector('#lilypad2');
const lilypad3 = document.querySelector('#lilypad3');
const lilypad4 = document.querySelector('#lilypad4');
const lilypad5 = document.querySelector('#lilypad5');

const e = (left, top, current, previous) => {
  console.log("hop");
  frogger.style.left = left;
  frogger.style.top = top;
  current.classList.add('active');
  previous.classList.remove('active');
};

const disp = () => {
  lilypad4.style.display = 'none';
};
const appear= () => {
  lilypad4.style.display= 'block';
};

const reset=() => {
  currentlily = 1;
  frogger.style.left = "17%";
  frogger.style.top = "50%";
  lilypad1.classList.add('active');
  lilypad2.classList.remove('active');
  lilypad3.classList.remove('active');
  lilypad4.classList.remove('active');
  lilypad5.classList.remove('active');
};

let disappear = setInterval(disp,1000);
let app = setInterval(appear,2000);

//var touchFroggo = touchEvent.touches;
frogger.addEventListener('click', () => {
  switch (currentlily) {
    case 1:e("33.5%", "24%", lilypad2, lilypad1);  break;
    case 2: e("50%", "50%", lilypad3, lilypad2);  break;
    case 3:
    if (lilypad4.style.display != 'none') {
      clearInterval(disappear);
      e("68%", "75%", lilypad4, lilypad3);
      break;
    };
      if (lilypad4.style.display = 'none') {
        reset();
      };

      break;
    case 4: e("83%", "50%", lilypad5, lilypad4); setInterval(disp, 1000); break;
    default:  break;
}
   currentlily += 1;
});

frogger.addEventListener('mouseover', (e) => {
  frogger.style.width = "80px";
  frogger.style.height = "80px";
});
frogger.addEventListener('mouseleave', (e) => {
  frogger.style.width = "70px";
  frogger.style.height = "70px";
});

document.addEventListener('keydown', (e) => {
  if (e.keyCode ==32) {
      reset();
    //lilypad2.classList.remove('active');
  }
});

// frogger.addEventListener('click', e("50%", "50%", lilypad3, lilypad2));
// frogger.addEventListener('click', e("68%", "75%", lilypad4, lilypad3));
// frogger.addEventListener('click', e("83%", "50%", lilypad5, lilypad4));
//alert("Congratulations! You won!");

// frogger.addEventListener('click',(e) => {
//   console.log("hop");
//   frogger.style.left = "50%";
//   frogger.style.top = "50%";
//   lilypad3.classList.add(' active');
// });
//
// frogger.addEventListener('click',(e) => {
//   console.log("hop");
//   frogger.style.left = "68%";
//   frogger.style.top = "75%";
//   lilypad3.classList.add(' active');
// });
//
// frogger.addEventListener('click',(e) => {
//   console.log("hop");
//   frogger.style.left = "68%";
//   frogger.style.top = "75%";
//   lilypad3.classList.add(' active');
// });

// frogger.addEventListener('touchstart', (e) => {
//   if (e.touchFroggo.length >=1) {
//     lilypad2.classList.add('active');
//   }
// });
