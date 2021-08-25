$("#ettoday_btn").click(function(){
    $("#ettoday").toggle(1000);
    $("#tvbs").hide(500);
    $("#udn").hide(500);
});

$("#tvbs_btn").click(function(){
    $("#tvbs").toggle(1000);
    $("#ettoday").hide(500);
    $("#udn").hide(500);
});

$("#udn_btn").click(function(){
    $("#udn").toggle(1000);
    $("#ettoday").hide(500);
    $("#tvbs").hide(500);
});