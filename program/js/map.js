function readTextFile(file, callback) {
    var rawFile = new XMLHttpRequest();
    rawFile.overrideMimeType("application/json");
    rawFile.open("GET", file, true);
    rawFile.onreadystatechange = function() {
        if (rawFile.readyState === 4 && rawFile.status == "200") {
            callback(rawFile.responseText);
        }
    }
    rawFile.send(null);
}

//usage:
readTextFile("D:/git_workplace/food/program/pig.json", function(text){
    var data = JSON.parse(text);
    console.log(data);
});

//win+r chrome.exe --allow-file-access-from-files

//地圖
let map;
document.addEventListener("DOMContentLoaded", () => {
let s = document.createElement("script");
        document.head.appendChild(s);
        s.addEventListener("load", () => {
            //script has loaded
            console.log("script has loaded");
            map = new google.maps.Map(document.getElementById("map"), {
                center: {
                    lat:23.695919378044756, 
                    lng: 120.53353474084176
                },
                zoom: 16,
                mapTypeId: google.maps.MapTypeId.ROADMAP
            });
        });
        s.src = `https://maps.googleapis.com/maps/api/js?key=AIzaSyDj79YdxxvDWfJ6ji3IEO31iTPrL8555vI&callback=initMap`; //請確定金鑰正確(AIzaSyDj79YdxxvDWfJ6ji3IEO31iTPrL8555vI)
});