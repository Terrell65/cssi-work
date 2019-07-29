let button = document.querySelector("#button");
let like_header = document.querySelector("#my-likes")
let like_count = 0;
button.addEventListener("click",()=> {
  like_count++;
  like_header.innerHTML = "YOU HAVE " + like_count + " likes.";
  console.log( "YOU HAVE " + like_count + "likes.");
});

const changeheadercolor = () => {
  like_header.style.color = "tomato";
}
like_header.addEventListener("click",changeheadercolor)
