jQuery = $ = require('jquery');

$(document).ready(function () {
    var menuSelectedClass = 'menu-selected';

    $('.menu-item').on('click', function () {
        if ($(this).hasClass(menuSelectedClass)) {
            $(this).removeClass(menuSelectedClass);
            return;
        }

        $('.' + menuSelectedClass).removeClass(menuSelectedClass);
        $(this).addClass(menuSelectedClass)
    });
});