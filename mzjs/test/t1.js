console.log("hello,world!")
const s = document.currentScript.src
console.log(s)
const xhr = new XMLHttpRequest();
xhr.open("GET", s)
xhr.onLoad = () => (console.log("success"))
xhr.send();