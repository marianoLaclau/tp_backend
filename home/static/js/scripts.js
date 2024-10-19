
document.getElementById('sidebarToggle').addEventListener('click', function() {
    var sidebar = document.getElementById('sidebar-wrapper'); // Asumiendo que tu sidebar tiene el ID "sidebar"
    var toggleIcon = document.getElementById('toggleIcon');

    // Alternar la visibilidad del sidebar
    if (sidebar.style.display === 'none' || sidebar.style.display === '') {
        sidebar.style.display = 'block';
        toggleIcon.classList.remove('bi-chevron-right');
        toggleIcon.classList.add('bi-chevron-left');
    } else {
        sidebar.style.display = 'none';
        toggleIcon.classList.remove('bi-chevron-left');
        toggleIcon.classList.add('bi-chevron-right');
    }
});
