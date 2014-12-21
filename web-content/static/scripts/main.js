$(document).ready(function() {


});

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
    else {
        if ($(window).scrollTop() - 5 > 0) {
            $('#jp-main-header').css({'box-shadow': '0px 2px 2px #888888'});
        }
        else {
            $('#jp-main-header').css({'box-shadow': 'none'});
        }
    }
});


/**
 * Función asociada
 */
function index_menu_mobile_slide () {

    if ($('.jp-main-header .content .menu').width()) {
        $('.jp-main-header .content .menu' ).removeClass( "menu-in", 400 );
        $('.jp-main-shadow' ).fadeOut(400);
    } else {
        $('.jp-main-header .content .menu' ).addClass( "menu-in", 400 );
        $('.jp-main-shadow' ).fadeIn(400);
    }
}