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

console.log("script is running...");
function My_alarm(wakeuptime) {
  return "Hey Terrell its " +wakeuptime;
};
console.log(My_alarm("6:00am"));

function kale_alarm(time2) {
  return "BOY WAKE UP " + time2;
};
console.log(kale_alarm("8:00am"));
function Family_alarm(time3,time4){
  return "Rell wake up " +time3+ "kale wake up " +time4;
};
console.log(Family_alarm("9:00am ","9:30am "));
const important_alarm = (message) => {
  return message.toUpperCase()
}
console.log(important_alarm(" wake up wake up wakeup"));
const snooze_alarm = (number) => {
  return "the alarm for " + number + " has been changed to "+(number+1);
}
console.log(snooze_alarm(1));
