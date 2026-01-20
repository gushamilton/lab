document.addEventListener("DOMContentLoaded", function () {
    // Only simplify layout on small screens
    if (window.innerWidth > 900) return;

    const notes = document.querySelectorAll('.marginnote, .marginnote-left, .sidenote');

    notes.forEach(note => {
        // Hide the note by default on mobile (CSS should handle this, but ensuring here)
        // note.style.display = 'none'; // Better handled by class toggle

        // Create the toggle button
        const toggle = document.createElement('span');
        toggle.className = 'margin-toggle-button';
        toggle.innerHTML = '⊕'; // Icon
        toggle.setAttribute('aria-label', 'Show note');
        toggle.setAttribute('role', 'button');

        // Insert button before the note
        note.parentNode.insertBefore(toggle, note);

        // Toggle functionality
        toggle.addEventListener('click', function (e) {
            e.preventDefault();
            e.stopPropagation();

            const isVisible = note.classList.contains('visible');

            if (isVisible) {
                note.classList.remove('visible');
                toggle.innerHTML = '⊕';
                toggle.classList.remove('active');
            } else {
                note.classList.add('visible');
                toggle.innerHTML = '⊖';
                toggle.classList.add('active');
            }
        });
    });
});
