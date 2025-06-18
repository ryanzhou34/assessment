

document.addEventListener('DOMContentLoaded', function() {
    const mobileToggle = document.querySelector('.menu-toggle');
    const mainNav = document.querySelector('.-menu');
    
    if (mobileToggle && mainNav) {
        mobileToggle.addEventListener('click', function() {
            mainNav.classList.toggle('active');
            mobileToggle.classList.toggle('active');
        });
    }
    

    const navLinks = document.querySelectorAll('.menu a');
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            if (window.innerWidth <= 768) {
                mainNav.classList.remove('active');
                mobileToggle.classList.remove('active');
            }
        });
    });
    
});
