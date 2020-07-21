'use strict';

(function ($) {
    
    /*------------------
        Slick Nav
    --------------------*/
    $(".main-menu").slicknav({
        prependTo: '#mobile-menu-wrap',
        allowParentLinks: true
    });

    /*------------------
        Preloader
    --------------------*/
    $(window).on('load', function () {
        $(".loader").fadeOut();
        $("#preloder").delay(400).fadeOut("slow");
    });

    /*------------------
        Background Set
    --------------------*/
    $('.set-bg').each(function () {
        var bg = $(this).data('setbg');
        $(this).css('background-image', 'url(' + bg + ')');
    });

    /*------------------
        Nice Select
    --------------------*/
    $(document).ready(function () {
        $('.filter-location').niceSelect();
    });

    $(document).ready(function () {
        $('.filter-property').niceSelect();
    });

    $(document).ready(function () {
        $('.date-select').niceSelect();
    });

    /*------------------
        Carousel Slider
    --------------------*/
    $('.slider-active').owlCarousel({
        items: 1,
        dots: false,
        nav: true,
        loop: true,
        navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"]
    });

    /*--------------------------------
        Property Image Carousel Slider
    -----------------------------------*/
    $('.property-img').owlCarousel({
        items: 1,
        dots: false,
        nav: true,
        loop: true,
        navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"]
    });

    /*--------------------------------
        Price Slider
    -----------------------------------*/
    $("#slider-range").slider({
        range: true,
        min: 50,
        max: 300,
        step: 50,
        value: 50,
        values: [50, 300],
        slide: function (event, ui) {
            $('#slider-range .slider-left').text(ui.values[0] + 'k');
            $('#slider-range .slider-right').text(ui.values[1] + 'k');
        }
    });

})(jQuery);