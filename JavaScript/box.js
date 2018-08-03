console.log("Hello");


let rightButton = document.querySelector("#right");
rightButton.addEventListener("click", e=> {
  let box = document.querySelector("#box");
  let currentLeft = box.style.left;
  let newLeft = parseInt(currentLeft) + 10;
  box.style.left = newLeft + "px";
})

let leftButton = document.querySelector("#left");
leftButton.addEventListener("click", e=> {
  let box = document.querySelector("#box");
  let currentLeft = box.style.left;
  let newLeft = parseInt(currentLeft) - 10;
  box.style.left = newLeft + "px";
})

let upButton = document.querySelector("#up");
upButton.addEventListener("click", e=> {
  let box = document.querySelector("#box");
  let currentTop = box.style.top;
  let newTop = parseInt(currentTop) - 10;
  box.style.top = newTop + "px";
})

let downButton = document.querySelector("#down");
downButton.addEventListener("click", e=> {
  let box = document.querySelector("#box");
  let currentTop = box.style.top;
  let newTop = parseInt(currentTop) + 10;
  box.style.top = newTop + "px";
})


let boxButton = document.querySelector("#box");
boxButton.addEventListener("click", e=> {
  boxButton.innerText = "👍 ";
  boxButton.disabled = true;
})
