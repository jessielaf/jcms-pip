// Adds the dropdown functionality for the user menu
(function () {
    $('.jcms-dropdown').on('click', function (e) {
        data = $(this).data();

        if (typeof data['dropdown_target'] === 'undefined') {
            return;
        }

        dropdownTarget = $('#' + data['dropdown_target']);
        currentDisplay = dropdownTarget.css('display');

        if (currentDisplay === 'none') {
            dropdownTarget.css('display', 'inherit');
        } else {
            dropdownTarget.css('display', 'none');
        }
    });
}());
