console.log("Hello!")

//Make a form for searching
//Get results for a search Engine
//Display gifs



//need an api key


let apiKey = "ABc4k9V7065fevCrUU5XnsIIJBmSkcNW";

let url = "http://api.giphy.com/v1/gifs/search";

function createImage(url) {
  let image = document.createElement("img");
  image.src = url;
  document.body.appendChild(image);
  console.log(result);
}

let go = document.querySelector("#go");
let input = document.querySelector("#q");

go.addEventListener("click", e=> {
  let q = input.value;
  fetchGif(q);
})

function fetchGif(searchTerm) {
  let query = `${url}?api_key=${apiKey}&q=${searchTerm}s&limit=1`;
  console.log(searchTerm);
  window.fetch(query).then(data => {
    return data.json();
  }).then(json => {
    let results = json.data;
    console.log(json.data);
    let result = results[0];
    console.log(result);
    createImage(result.images.downsized.url);

  });
}
