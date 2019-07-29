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

const changeotherboxcolors2 = () => {
  box1.style.backgroundColor = "grey";
  box2.style.backgroundColor = "maroon"

};

box1.addEventListener("click",changeotherboxcolors2);
console.log("Running Click Events Script");
const box1 = document.querySelector("#box1");
const box2 = document.querySelector("#box2");
const box3 = document.querySelector("#box3");

const changeotherboxcolors = (color) => {
  console.log("hello")
  box1.style.backgroundColor = color;
  box2.style.backgroundColor = color;
  box3.style.backgroundColor = color;
}
box1.addEventListener("click",() => {
  changeotherboxcolors("red");
});
 box2.addEventListener("click",()=> {
  changeotherboxcolors("pink");
 });
 box3.addEventListener("click",() => {
   changeotherboxcolors("orange");
 });



const box4 = document.querySelector("#box4");
box4.addEventListener("click", () => {
  box4.classList.toggle("active");
// })
