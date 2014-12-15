$(window).scroll(function() {
   if($(window).scrollTop() - 40 > 0) {
       $('#jp-main-header').css({'height': '30px'});
       $('#jp-main-header .content').css({'height': '30px'});
       $('#jp-main-header .content .logo').css({'font-size': '15px'});
   }
   else {
       $('#jp-main-header').css({'height': '70px'});
       $('#jp-main-header .content').css({'height': '70px'});
       $('#jp-main-header .content .logo').css({'font-size': '32px'});
   }
});
