// Closes the parent element by giving it display none
(function () {
    $('.alert .icon').on('click', function () {
        $(this).parent().css('display', 'none');
    });
}());
