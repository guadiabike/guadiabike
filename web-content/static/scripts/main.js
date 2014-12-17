$(window).scroll(function() {

    if($('#large-mode').is(':visible')) {
        if ($(window).scrollTop() - 35 > 0) {
            $('#jp-main-header').css({'height': '30px'}).css({'box-shadow': '0px 2px 2px #888888'});
            $('#jp-main-header .content').css({'height': '30px'});
            $('#jp-main-header .content .logo').css({'font-size': '1.4em'});
        }
        else {
            $('#jp-main-header').css({'height': '70px'}).css({'box-shadow': 'none'});
            $('#jp-main-header .content').css({'height': '70px'});
            $('#jp-main-header .content .logo').css({'font-size': '2.5em'});
        }
    }
});
