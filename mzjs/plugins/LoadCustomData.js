console.log("start load custom data.");



function Game_Custom() {
    this.initialize(...arguments);
}

Game_Custom.prototype.initialize = function () {
    this._hello = null;
    this._title = "";
    this._number = 0;
}
Game_Custom.prototype.hello = () => {
    return window[$dataCustomData].hello
}

var $dataCustomData = new Game_Custom();


const custom_url = "data/Customs.json"
console.log("loading:", $dataCustomData);

const xhr = new XMLHttpRequest();
xhr.open("GET", custom_url);
xhr.overrideMimeType("application/json");
xhr.onload = function () {
    if (xhr.status < 400) {
        window[$dataCustomData] = JSON.parse(xhr.responseText);
        console.log(xhr.responseText);
    }
}
xhr.onerror = () => console.log("Error.");
xhr.send();


console.log("load over.Hello:", $dataCustomData)


function p(msg) {
    console.log(msg);
}