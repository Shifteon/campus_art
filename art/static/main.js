/**
 *   Function to display the categories
 */
function displayCategories() {
    let btns = document.querySelectorAll('.category-btn');
    let categories = document.querySelectorAll('.categories');
    // console.log(btns.length);
    // console.log(categories.length);
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

function moveSideThing() {
    let sideThing = document.querySelector('.side-thing');
    let nav = document.querySelector('nav');
    let top = 0;

    window.addEventListener('scroll', () => {
        let scroll = window.scrollY;
        if (scroll > 375) {
            sideThing.style.top = `${scroll - 375 + 10}px`;
        } else {
            sideThing.style.top = "0";
        }
    });
}

function openFilter() {
    const btn = document.querySelector('#filter-extend');
    const filter = document.querySelector('.side-thing');

    btn.addEventListener('click', () => {
        filter.classList.toggle('open');
        if (filter.classList.contains('open'))
            btn.innerHTML = '-';
        else
            btn.innerHTML = '+';
    });
}

function openNav() {
    // Create responsive nav
    const hambutton = document.querySelector('.ham');
    const mainnav = document.querySelector('#navigation');

    hambutton.addEventListener('click', () => {
        mainnav.classList.toggle('responsive');
    }, false);
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
            btn.innerHTML = '-';
        } else {
            btn.innerHTML = '+';
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

function buildingsDropdown() {
    const dropDown = document.querySelector('#buildings-dropdown');
    const nav = document.querySelector('#buildings-link');

    nav.addEventListener('click', () => {
        dropDown.classList.toggle('display');

        window.onclick = (event) => {
            console.log("Target: " + event.target);
            if (event.target == dropDown) {
                console.log("hi");
                dropDown.classList.remove('display');
            }
        }
    });
}

/**
 *   Called when the window is loaded.
 *   Basically our 'main' function.
 */
window.addEventListener('load', () => {
    openNav();
    buildingsDropdown();
    createid();
    displayCategories();
    displayFilterCategories();
    moveSideThing();
    openFilter();
    smallFilter();
})