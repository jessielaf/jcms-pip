jQuery = $ = require('jquery');

$(document).ready(function () {
    var menu_selected_class = 'menu-selected';

    $('.menu-item').on('click', function () {
        var opening = true;

        if ($(this).hasClass(menu_selected_class)) {
            opening = false;
        }

        $('.' + menu_selected_class).removeClass(menu_selected_class);

        if (opening) {
            $(this).addClass(menu_selected_class)
        }
    });
});