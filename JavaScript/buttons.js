console.log("Hello");

let likeButton = document.querySelector("#likeButton");
console.log(likeButton);

//can only use the e inside the curly braces
likeButton.addEventListener("click", e => {
  likeButton.innerText = "👍 ";
  likeButton.disabled = true;
});

let growButton = document.querySelector("#growButton");

growButton.addEventListener("click", e => {
  console.log("Click!");
  let currentSize = growButton.style.fontSize;
  let newSize = parseInt(currentSize) + 10;
  growButton.style.fontSize = newSize + "px";
  
})
