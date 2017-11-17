jQuery = $ = require('jquery');

$(document).ready(function () {
    userMenu();
    mobileMenu();

    function userMenu() {

        $('.menu-item').on('click', function () {
            var menuSelectedClass = 'menu-selected';
            
            if ($(this).hasClass(menuSelectedClass)) {
                $(this).removeClass(menuSelectedClass);
                return;
            }

            $('.' + menuSelectedClass).removeClass(menuSelectedClass);
            $(this).addClass(menuSelectedClass)
        });
    }

    function mobileMenu() {

        $('.mobile-menu').on('click', function () {
            var sideNav = $('.side-nav');
            var content = $('.content');
            
            var menuOpenClass = 'show-menu';
            var hiddenContent = 'hidden-content';

            if (sideNav.hasClass(menuOpenClass)) {
                sideNav.removeClass(menuOpenClass);
                content.removeClass(hiddenContent);
            } else {
                sideNav.addClass(menuOpenClass);
                content.addClass(hiddenContent);
            }
        });
    }
});
