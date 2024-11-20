// Get all links in the navbar
const navLinks = document.querySelectorAll(".nav-link");

// Get the current page URL
const currentPage = window.location.pathname;

// Loop through links and add 'active' to the matching link
navLinks.forEach(link => {
  if (link.getAttribute("href") === currentPage) {
    link.classList.add("active");
  }
});
