// This adds the switching for the menu items and the openings of the menu items
(function () {
    $('.menu-item').on('click', function () {
        var menuSelectedClass = 'menu-selected';

        if ($(this).hasClass(menuSelectedClass)) {
            $(this).removeClass(menuSelectedClass);
            return;
        }

        $('.' + menuSelectedClass).removeClass(menuSelectedClass);
        $(this).addClass(menuSelectedClass)
    });
}());
