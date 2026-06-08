console.log("JS LOADED");

document.addEventListener("DOMContentLoaded", () => {

    const options = document.querySelectorAll(".escape-option");

    options.forEach(option => {

        option.addEventListener("mouseover", () => {

            const maxX = window.innerWidth - option.offsetWidth;
            const maxY = window.innerHeight - option.offsetHeight;

            const randomX = Math.random() * maxX;
            const randomY = Math.random() * maxY;

            option.style.position = "fixed";
            option.style.left = randomX + "px";
            option.style.top = randomY + "px";
        });

    });

});