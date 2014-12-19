$(document).ready(function() {

    // Eventos.
    $('#jp-main-header-button-menu').click(index_menu_mobile_slide);

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

    if ($('#jp-menu-mobile').is(":visible")) {
        $('#jp-main-shadow').animate({
          opacity: 0.10
        }, 300, function() {
            $('#jp-main-shadow').hide();
        });
        $('#jp-menu-mobile')
        .stop()
        .animate({
          width: "0",
          opacity: 0.1
        }, 300, function(){
            $('#jp-menu-mobile').hide();
        });

    } else {
        $('#jp-main-shadow').show().animate({
          opacity: 0.80
        }, 300);
        $('#jp-menu-mobile').show()
        .stop()
        .animate({
          width: "90%",
          opacity: 0.99
        }, 300, function(){});
    }
}