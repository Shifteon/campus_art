document.addEventListener('DOMContentLoaded', function () {

var detail_grid = document.querySelector('#detail-grid');
detail_image = document.querySelector('#detail-image');
large_div = document.querySelector('#viewport_size');
large_image = document.querySelector('#large-image');

detail_image.addEventListener("click", () => {
    detail_grid.style.display = 'none';
    large_div.style.display = 'block';
})


large_image.addEventListener("click", () => {
    detail_grid.style.display = 'grid';
    large_div.style.display = 'none';
})

})