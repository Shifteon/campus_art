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
    window.addEventListener('scroll', () => {
        let scroll = window.scrollY;
        if (scroll > 64) {
            sideThing.classList.add('past-nav');
        } else {
            sideThing.classList.remove('past-nav');
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
    moveSideThing();
})