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


$(function() {

    var map = document.getElementById("map");
          
    var latlng = new google.maps.LatLng(23.695919378044756, 120.53353474084176);
          
    var mapOptions = {
        zoom: 16,
        center: latlng,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        scrollwheel: false
    };
          
    var mapObj = new google.maps.Map(map, mapOptions);
    var marker = [];
    var infoWindow = [];
          
    // 地圖標記
    var markerData = [
            {
                position: new google.maps.LatLng(23.6904173, 120.5289109),
                title: '測試',
                content: '我家對面啦',
                icon: 'https://i.imgur.com/PKdLaxG.png',
            },
            {
                position: new google.maps.LatLng(23.693625, 120.5274303),
                title: '萊爾富',
                content: 'ㄚ就萊爾富',
                icon: 'https://i.imgur.com/PKdLaxG.png',
            }
    ];
          
            // 標記在地圖上
            for (i = 0; i< markerData.length; i++) {
              marker[i] = new google.maps.Marker({
                position: markerData[i].position,
                map: mapObj,
                title: markerData[i].title,
                icon: markerData[i].icon,
              });
          
              infoWindow[i] = new google.maps.InfoWindow({ // 訊息框
                content: '<div class="name">' + markerData[i]['title']+'<br>'+ markerData[i]['content'] + '</div>'
              });
              
              markerEvent(i);
            }
            
            // 標記訊息框
            function markerEvent(i) {
              marker[i].addListener('click', function() {
                infoWindow[i].open(mapObj, marker[i]);
              });
            }
            
            // 餐廳搜尋 - 他有點問題但我暫時找不到
            $('.form-inline').submit(function() {
              setAddress($('.form-control').val());
              return false;
            });
          
            
            function setAddress(address) {
                var sad = address;
                var geocoder = new google.maps.Geocoder();
                geocoder.geocode({'address':sad}, function(results, status) {
                    if (status == google.maps.GeocoderStatus.OK) {
                        mapObj.setCenter(results[0].geometry.location);
                    } else {
                        alert('找不到');
                    }
                });
            }
          
});