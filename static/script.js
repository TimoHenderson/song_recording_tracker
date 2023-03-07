document.addEventListener('DOMContentLoaded', () => {
    const menuButton = document.querySelector("#menu-button");
    menuButton.addEventListener("click", handleMenuButton);
    const navPane = document.querySelector("#nav-pane");
    navPane.addEventListener("click", handleNavPane);

    const cardMenuButtons = document.querySelectorAll(".card-menu-button");
    cardMenuButtons.forEach(cardMenuButton => cardMenuButton.addEventListener("click", handleCardMenuButton));

    const modalButtons = document.querySelectorAll(".modal-button");
    modalButtons.forEach(modalButton => modalButton.addEventListener("click", handleModalButton));

    const modals = document.querySelectorAll(".modal");
    modals.forEach(modal => modal.addEventListener("click", handleClickOutside));

    const closeModalButtons = document.querySelectorAll(".close-modal");
    closeModalButtons.forEach(button => button.addEventListener("click", handleCloseModals))
})

function handleClickOutside(event) {
    if (event.target.classList == "modal show") {
        event.target.classList = "modal";
        document.body.style.removeProperty('overflow');
    }
}

function handleCloseModals(event) {
    const openModals = document.querySelectorAll(".modal.show");
    openModals.forEach(openModal => openModal.classList = "modal")
}

function handleModalButton(event) {
    let modal;
    if (event.target.tagName === "BUTTON") {
        modal = event.target.nextElementSibling;
    } else {
        modal = event.target.parentNode.nextElementSibling;
    }
    modal.classList = "modal show";
    document.body.style.overflow = 'hidden';
    modal.style.overflow = 'scroll';
}

function handleMenuButton() {
    const navPane = document.querySelector("#nav-pane");
    const links = document.querySelectorAll('nav a');
    if (navPane.className === "") {
        navPane.className = "show";
        links.forEach(link => link.tabIndex = 0);
        document.body.style.overflow = 'hidden';
        document.querySelector("nav").style.overflow = 'scroll';
    } else {
        navPane.className = "";
        links.forEach(link => link.tabIndex = -1);
        document.body.style.removeProperty('overflow');
    }

}

function handleNavPane(event) {
    event.target.classList = "";
    document.body.style.removeProperty('overflow');
}

function handleCardMenuButton(event) {
    const cardMenu = event.target.parentNode.parentNode.nextElementSibling;
    if (cardMenu.classList == "card-menu") {
        const cardMenus = document.querySelectorAll(".card-menu");
        cardMenus.forEach(cardMenu => cardMenu.classList = "card-menu");
        const cardButtons = document.querySelectorAll(".close-card-menu");
        cardButtons.forEach(cardButton => cardButton.classList = "fa-solid fa-ellipsis-vertical fa-2x open-card-menu")
        cardMenu.classList = "card-menu show";
        event.target.classList = "fa-solid fa-ellipsis fa-2x close-card-menu";
    } else {
        cardMenu.classList = "card-menu";
        event.target.classList = "fa-solid fa-ellipsis-vertical fa-2x open-card-menu";
    }
}