$(document).ready(function() {
    $('.choose_list').delay(300).fadeIn();
    $('.choose_list p').click(function() {
        $(this).fadeOut();
    });
    $('#selector p input').click(function() {
        $(this).parent().fadeOut();
    });
    $('.product-width-fix').mouseenter(function() {
       $(this).children().fadeIn();
    });
    $('.product-width-fix').mouseleave(function() {
       $(this).children().fadeOut();
    });

});