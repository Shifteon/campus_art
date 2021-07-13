/**
 *   Function to display the categories
 */
function displayCategories() {
    let btns = document.querySelectorAll('.category-btn');
    let categories = document.querySelectorAll('.categories');
    
    for (let btn of btns) {
        btn.addEventListener('click', () => {
            let num = btn.id;
            categories[num].classList.toggle('display');
            if (categories[num].classList.contains('display')) {
                btn.innerHTML = "Categories -";
            } else {
                btn.innerHTML = "Categories +";
            }
        });
    }
}

/**
 *   The following is a function to add an id to every edit
 *   button so they correspond with the correct note.
 */
function createid() {
    // Add an incremented unique id to every edit button
    // This is so we know which form to display in edit()
    let btns = document.querySelectorAll(".category-btn");
    let btnNum = 0;
    for (btn of btns) {
        btn.id = btnNum;
        btnNum++;
    }
}

function displayFilterCategories() {
    let btn = document.querySelector('.filter-category-btn');
    let categories = document.querySelector('.filter-category');
    btn.addEventListener('click', () => {
        categories.classList.toggle('display');
        if (categories.classList.contains('display')) {
            btn.innerHTML = "Categories -";
        } else {
            btn.innerHTML = "Categories +";
        }
    });
}

function moveSideFilter() {
    let sideFilter = document.querySelector('.side-filter');
    let nav = document.querySelector('nav');
    let height = document.querySelector('header').clientHeight + nav.clientHeight + 48;
    console.log(height);

    window.addEventListener('scroll', () => {
        let scroll = window.scrollY;
        if (scroll > height) {
            sideFilter.style.top = `${scroll - height + 10}px`;
        } else {
            sideFilter.style.top = "0";
        }
    });
}

function openFilter() {
    const btn = document.querySelector('#filter-extend');
    const filter = document.querySelector('.side-filter');

    btn.addEventListener('click', () => {
        filter.classList.toggle('open');
        if (filter.classList.contains('open'))
            btn.innerHTML = '-';
        else
            btn.innerHTML = '+';
    });
}

function smallFilter() {
    const btn = document.querySelector('#filter-btn');
    const filter = document.querySelector('.small-filter');
    const filterBtn = document.querySelector('.small-filter-category-btn');
    const smallFilter = document.querySelector('.small-filter-category');

    btn.addEventListener('click', () => {
        filter.classList.toggle('display');
        btn.classList.toggle('clicked');
        if (btn.classList.contains('clicked')) {
            btn.innerHTML = '<span class="material-icons">clear</span>';
        } else {
            btn.innerHTML = '<span class="material-icons">add</span>';
        }
    });

    filterBtn.addEventListener('click', () => {
        smallFilter.classList.toggle('display');
        if (smallFilter.classList.contains('display')) {
            filterBtn.innerHTML = 'Categories -';
        } else {
            filterBtn.innerHTML = 'Categories +';
        }
    });
}

/**
 *   Called when the window is loaded.
 *   Basically our 'main' function.
 */
window.addEventListener('load', () => {
    createid();
    displayCategories();
    displayFilterCategories();
    moveSideFilter();
    openFilter();
    smallFilter();
})