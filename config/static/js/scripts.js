document.addEventListener('DOMContentLoaded', function() {
    var sidebarOpen = true; 

    function toggleSidebar() {
        var sidebar = document.getElementById("sidebar");
        var mainContent = document.getElementById("main-content");
        var sidebarSeparator = document.getElementById("sidebar-separator"); 


        if (sidebarOpen) {
            sidebar.style.left = "0px"; 
            mainContent.style.marginLeft = "250px";
            sidebarOpen = false; 
        } else {
            sidebar.style.left = "-250px";
            mainContent.style.marginLeft = "0";
            sidebarSeparator.style.display = "none"; 
            sidebarOpen = true; 
        }
    }

    function adjustSidebarHeight() {
        const sidebarContent = document.getElementById('sidebar-content');
        const authLinks = document.querySelector('.auth-links');
        const sidebar = document.querySelector('.sidebar');

        const authLinksHeight = authLinks.offsetHeight;
        const sidebarHeight = window.innerHeight;

        sidebarContent.style.height = `${sidebarHeight - authLinksHeight - 60}px`;
        sidebarContent.style.overflowY = 'auto';
    }

    window.addEventListener('resize', adjustSidebarHeight);
    window.addEventListener('load', adjustSidebarHeight);

    document.getElementById('sidebar-toggle-btn').addEventListener('click', toggleSidebar);

    toggleSidebar(); 
});



const signupContainer = document.getElementById('signup-container');
const loginContainer = document.getElementById('login-container');

function showSignupForm() {
    signupContainer.style.transform = 'translateX(0)';
    loginContainer.style.transform = 'translateX(100%)';
}

function showLoginForm() {
    signupContainer.style.transform = 'translateX(-100%)';
    loginContainer.style.transform = 'translateX(0)';
}


$(document).ready(function() {
    // Smooth scrolling for anchor links
    $('a[href^="#"]').on('click', function(event) {
        var target = $(this.getAttribute('href'));
        if( target.length ) {
            event.preventDefault();
            $('html, body').stop().animate({
                scrollTop: target.offset().top
            }, 1000);
        }
    });

    $('.carousel').carousel();

    var audio = document.getElementById('background-music');
    $('.music-toggle').click(function() {
        if (audio.paused) {
            audio.play();
            $(this).text('Pause Music');
        } else {
            audio.pause();
            $(this).text('Play Music');
        }
    });
});

