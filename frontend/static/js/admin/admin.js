document.addEventListener('DOMContentLoaded', function() {
    // Lấy tất cả các thẻ <details>
    const detailsElements = document.querySelectorAll('details');

    // Duyệt qua tất cả các thẻ và xóa thuộc tính "open"
    detailsElements.forEach(function(details) {
        details.removeAttribute('open');
    });
});
