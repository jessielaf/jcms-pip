// This adds the javascript for the mobile menu. It adds the right classes
(function () {
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
}());
