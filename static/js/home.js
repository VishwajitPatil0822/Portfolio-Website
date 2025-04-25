function showDropdowns() {
    document.getElementById("myDropdowns").style.display = "block";
}
function hideDropdowns() {
    document.getElementById("myDropdowns").style.display = "none";
}

function tandsshowDropdown(el) {
    const dropdown = el.querySelector(".dropdown-box");
    if (dropdown) dropdown.style.display = "block";
}

function tandshideDropdown(el) {
    const dropdown = el.querySelector(".dropdown-box");
    if (dropdown) dropdown.style.display = "none";
}
