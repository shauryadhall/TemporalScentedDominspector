
document.getElementById('contactForm').addEventListener('submit', function(e) {
  e.preventDefault();
  const email = this.querySelector('input[type="email"]').value;
  alert('Thank you for your interest! We will contact you soon at ' + email);
  this.reset();
});

// No carousel animation needed for grid layout
