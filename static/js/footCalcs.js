function footerCalc() {
    $("footer").css({
            "position" : "absolute",
            "top" : $("body").height() + 76 ,
            "width": "100vw",
        })
 }

$(document).ready(() => {
    footerCalc();
})

window.onresize = footerCalc;