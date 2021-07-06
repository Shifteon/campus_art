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

function openNav() {
    // Create responsive nav
    const hambutton = document.querySelector('.ham');
    const mainnav = document.querySelector('#navigation');

    hambutton.addEventListener('click', () => {
        mainnav.classList.toggle('responsive');
    }, false);
}

window.addEventListener('load', () =>{
    openNav();
    buildingsDropdown();
});