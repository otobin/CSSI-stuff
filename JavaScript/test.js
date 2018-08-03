console.log("hello");

let name = "Julia";
let daysLeft = 5;
console.log("Hello, " + name + ". ");
console.log("There are " + daysLeft + " days left in CSSI.")

if (daysLeft < 6)
{
  console.log("You are in the final project week. Good luck on your final project.")
}

while(daysLeft < 6)
{
  console.log(daysLeft)
  daysLeft ++
}
// check if the name is Julia or Jess and say you're a site lead
if (name == "Matthew" || name == "Rachel" || name == "Ciera")
{
  console.log("You are an instructor.");
} else if (name == "Stephanie" || name == "Logan" || name == "Sharon") {
  console.log("You are a TA");
} else if (name == "Julia" || name == "Jess") {
  console.log("You are a site lead");
}
else {
  console.log("You are a studnet");
}


if (daysLeft < 6 && name == "Olivia") // This is a comment
{
  console.log("Remember to do your final projects.");

}

//1.) Tell the loop when to start: initialization ( i = 0)
//2.) Tell teh loop when to stop: (i < 100)
//3.) What to do for each loop (i ++)

for (let i = 10; i >= 0; i --)
{
  console.log(i);
}
console.log("Blastoff!");

//DRY = don't repeat yourself!


// function
function greet(name){
  console.log("Welcome, " + name + "!");
}

function fullName(firstName, lastName) {
  return firstName + " " + lastName;
}

greet(fullName("Olivia", "Tobin"))


fullName("Olivia", "Tobin")

greet("Olivia");

function square(int) {
  return int * int;
}

square(4);

function fourthPow(int) {
  let stepOne = square(int);
  let stepTwo = square(int);
  return stepOne * stepTwo;;
}

console.log(fourthPow(2));

function pythagorean(a, b) {
  return square(a) + square(b)
}

console.log(pythagorean(4, 5));
