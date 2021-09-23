window.addEventListener("load", function () {
    let letter_li = document.querySelectorAll(".letter");
    letter_li.forEach((li) =>
        li.addEventListener("click",function(){
            displayShows(li.getAttribute("id"))
        }))
})


function displayShows(letter) {
    fetch(`/api/shows/${letter}`)
        .then(response => response.json())
        .then(data =>{
            let shows_div = document.getElementById("shows")
            shows_div.innerHTML = ""
            let html = ""
            data.forEach((d) => html += `<div>${d["title"]} ${d["year"]} ${d["episode_count"]}</div>`)
            shows_div.innerHTML = html
        })
}