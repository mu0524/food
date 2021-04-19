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
/*
var map;
function initMap() {
    var position = {
      lat: 23.695919378044756,
      lng: 120.53353474084176
    };
    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 18,
      center: position
    });
    var marker = new google.maps.Marker({
      position: position,
      map: map
    });
  }*/

//win+r chrome.exe --allow-file-access-from-files