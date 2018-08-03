

console.log("Hello!");

/*
let scores = [97, 92, 90, 87, 88, 100, 99, 105];

let max = scores[0];
let total = 0;
for (let i = 0; i < scores.length; i ++) {
  total += scores[i];
  if (scores[i] > max) {
    max = scores[i];
  };
}
console.log("The maximum value in the scores array is " + max)
console.log("The total value of all the scores in the array is " + total);
console.log("The average value of all the scores is " + total/scores.length);

let names = ["Savion", "Jenny", "Olivia", "Joshua"];

names.forEach(name => { //How to write a for each loop in JavaScript
  console.log("Hello, " + name);
})
*/

//let matthew = ["Matthew", "Levine", "Dartmouth", "Harry Potter"];

//let yojairo = ["Yojairo", "Morales", "USC", "Kendrick Lamar"];


//Objects can hold multiple pieces of data, defined by curly braces

let matthew = {
  "firstName": "Matthew",
  "lastName": "Levine",
  "university": "Dartmouth",
  "culture": "Harry Potter"
}

console.log(matthew.university);

let yojairo = {
  "firstName": "Yojairo",
  "lastName": "Morales",
  "university": "USC",
  "culture": "Kendrick Lamar",
}

let people = [matthew, yojairo];

people.forEach(person => {
  console.log(person.firstName + " really likes " + person.culture);
})


//scores.pop() --> pops the last element off the array
//scores.push() --> pushes a score at the

//scores.splice(1, 1, 94) --> first number is index of added, second number is
//index of thing deleted, third is the value of added
