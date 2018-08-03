console.log("Hello!");


let boxes = document.querySelectorAll("div");
console.log(boxes);

boxes.forEach(box => {

  box.addEventListener("mouseover", e=> {
    box.classList.add("spin");
  });


  box.addEventListener("mouseleave", e=> {
    box.classList.remove("spin");
  });
})


window.addEventListener("keypress", e => {
  if (e.key == "g" || e.key == "G") {
    boxes.forEach(box => {
      box.classList.remove("red");
      box.classList.add("green");
    })
  }
    if (e.key == "b" || e.key == "B") {
      boxes.forEach(box => {
        box.classList.remove("red");
        box.classList.remove("green")
        box.classList.add("blue");
    })
  }
    if (e.key == "r" || e.key == "R") {
      boxes.forEach(box => {
        box.classList.remove("green")
        box.classList.remove("blue");
        box.classList.add("red");
    })
  }
});
