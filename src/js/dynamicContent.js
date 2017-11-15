$(document).ready(function () {
    var contentContainer = $('.content');

    $('.option').on('click', function () {
        var path = $(this).data()['data-path'];

        contentContainer.innerhtml($.get(path));
    });
});
