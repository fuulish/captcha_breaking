// ==UserScript==
// @name         Albert and Marie
// @namespace    Malbertie
// @version      0.1
// @description  Insert text descriptions next to Albert and Marie
// @author       David Sean
// @include      https://journals.aps.org/*
// @run-at      document-idle
// ==/UserScript==

window.addEventListener('load', function() {

    var section = document.getElementById("title");
    //alert(section2.innerHTML);
    var x  = section.nextSibling;
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



function verify_image(captcha) {
    var canvas = document.createElement('canvas');
    canvas.width = captcha.width;
    canvas.height = captcha.height;
    var contour = captcha.width+captcha.height;
    canvas.getContext('2d').drawImage(captcha, 0, 0, captcha.width, captcha.height);
    var is_marie = false;
    var is_albert = false;

    //var ave = 0;
    // travel down the pixels and convert to greyscale
    //for (i=0; i<captcha.width/100; i++){
    //    for (j=0; j<captcha.height/100; j++) {
    //        var pixel = canvas.getContext('2d').getImageData(i, j, 1, 1).data;
    //        var greyscale = (pixel[0]+pixel[1]+pixel[2])/3;
    //        ave = ave + 1;
    //        // append to image array here
    //    }
    //}
    //ave = float(ave)/(captcha.width*captcha.height);
    marie_px=[40,40,39,255];
    albert_px=[100,100,100,255];
    var pixel = canvas.getContext('2d').getImageData(0+1, captcha.height-1, 1, 1).data;
    var result = "nope,";

    is_marie = is_close(pixel, marie_px, 15) ;
    is_albert = is_close(pixel, albert_px, 15);

    if (is_marie || is_albert) {
        result = "yes!";
    }
    return result;
}

function is_close(one,two,tol){
    if (Math.abs(one.reduce(add, 0)-two.reduce(add, 0))<tol) {
        return true;
    } else {
        return false;
    }
}

function add(a, b) {
    return a + b;
}



