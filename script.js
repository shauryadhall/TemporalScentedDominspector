
document.getElementById('contactForm').addEventListener('submit', function(e) {
  e.preventDefault();
  const email = this.querySelector('input[type="email"]').value;
  alert('Thank you for your interest! We will contact you soon at ' + email);
  this.reset();
});

// Simple carousel animation
const carousel = document.querySelector('.carousel');
setInterval(() => {
  carousel.scrollBy({
    left: 220,
    behavior: 'smooth'
  });
  if (carousel.scrollLeft >= carousel.scrollWidth - carousel.clientWidth) {
    carousel.scrollTo({
      left: 0,
      behavior: 'smooth'
    });
  }
}, 3000);
