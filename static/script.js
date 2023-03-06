document.addEventListener('DOMContentLoaded', () => {
    const menuButton = document.getElementById("menu-button");
    menuButton.addEventListener("click", handleMenuButton);

    const cardMenuButtons = document.querySelectorAll(".card-menu-button")
    cardMenuButtons.forEach(cardMenuButton => cardMenuButton.addEventListener("click", handleCardMenuButton));

    const modalButtons = document.querySelectorAll(".modal-button")
    modalButtons.forEach(modalButton => modalButton.addEventListener("click", handleModalButton))

    const modals = document.querySelectorAll(".modal")
    modals.forEach(modal => modal.addEventListener("click", handleClickOutside));
})

function handleClickOutside(event) {
    event.target.classList = "modal";
    document.body.style.removeProperty('overflow');
}

function handleModalButton(event) {
    const modal = event.target.parentNode.nextElementSibling;
    modal.classList = "modal show";
    document.body.style.overflow = 'hidden';
}

function handleMenuButton() {
    const navPane = document.querySelector("#nav-pane");
    const links = document.querySelectorAll('nav a');
    if (navPane.className === "") {
        navPane.className = "show";
        links.forEach(link => link.tabIndex = 0);
    } else {
        navPane.className = "";
        links.forEach(link => link.tabIndex = -1);
    }
}

function handleCardMenuButton(event) {
    const cardMenus = document.querySelectorAll(".card-menu");
    cardMenus.forEach(cardMenu => cardMenu.classList = "card-menu");
    const cardMenu = event.target.parentNode.parentNode.nextElementSibling;
    if (cardMenu.classList == "card-menu") {
        cardMenu.classList = "card-menu show";
        event.target.classList = "fa-solid fa-ellipsis fa-2x close-card-menu";
    } else {
        cardMenu.classList = "card-menu";
        event.target.classList = "fa-solid fa-ellipsis-vertical fa-2x open-card-menu";
    }
}