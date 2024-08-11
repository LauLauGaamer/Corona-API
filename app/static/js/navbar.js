document.addEventListener("DOMContentLoaded", function() {
    const dropdownItem = document.getElementById('dropdownItem');
    const dropdownMenu = dropdownItem.querySelector('.dropdown-menu');
    let timer;

    function showDropdown() {
        clearTimeout(timer);
        dropdownItem.classList.add('show');
    }

    function hideDropdown() {
        timer = setTimeout(function() {
            dropdownItem.classList.remove('show');
        }, 500);
    }

    dropdownItem.addEventListener('mouseenter', showDropdown);
    dropdownMenu.addEventListener('mouseenter', showDropdown);

    dropdownItem.addEventListener('mouseleave', hideDropdown);
    dropdownMenu.addEventListener('mouseleave', hideDropdown);
});