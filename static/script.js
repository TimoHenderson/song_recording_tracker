document.addEventListener('DOMContentLoaded', () => {
    const menuButton = document.getElementById("menu-button");
    menuButton.addEventListener("click", handleMenuButton);
})

function handleMenuButton() {
    const navPane = document.getElementById("nav-pane");
    const links = document.querySelectorAll('nav a');
    if (navPane.className === "") {
        navPane.className = "show";
        links.forEach(link => link.tabIndex = 0);
    } else {
        navPane.className = "";
        links.forEach(link => link.tabIndex = -1);
    }
}