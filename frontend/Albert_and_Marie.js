// ==UserScript==
// @name         Albert and Marie
// @namespace    Malbertie
// @version      0.1
// @description  Insert text descriptions next to Albert and Marie
// @author       David Sean
// @include      https://journals.aps.org/*/pdf/* 
// @run-at       document-idle
// ==/UserScript==

// use this to wait untill the page has completely loaded
window.addEventListener('load', function() {

    var section = document.getElementById("title");
    var captcha_form = document.forms.item(1);
    var button = captcha_form.childNodes[0].childNodes;
    for (i = 0; i < button.length-3; i++) {
        var captcha_id = button[i].childNodes[0].value;
        var captcha = document.getElementById(captcha_id);
        var under_text = document.createTextNode(verify_image(captcha));
        var h = document.createElement("H1");
        h.appendChild(under_text);
        button[i].childNodes[0].appendChild(h);
    }

}, false);


// currently just returns a dummy string
function verify_image(captcha) {
    var canvas = document.createElement('canvas');
    canvas.width = captcha.width;
    canvas.height = captcha.height;
    var contour =captcha.width+captcha.height;
    canvas.getContext('2d').drawImage(captcha, 0, 0, captcha.width, captcha.height);
    var ave = 0;
    // travel to the pixels and convert to greyscale
    //for (i=0; i<captcha.width/100; i++){
    //    for (j=0; j<captcha.height/100; j++) {
    //        var pixel = canvas.getContext('2d').getImageData(i, j, 1, 1).data;
    //        var greyscale = (pixel[0]+pixel[1]+pixel[2])/3;
    //        ave = ave + 1;
    //        // append to image array here
    //    }
    //}
    //ave = float(ave)/(captcha.width*captcha.height);
    return " nope: "+ contour.toString()+"px ";
}
