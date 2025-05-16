
document.getElementById('contactForm').addEventListener('submit', function(e) {
  e.preventDefault();
  const email = this.querySelector('input[type="email"]').value;
  
  fetch('/submit-email', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ email: email })
  })
  .then(response => response.json())
  .then(data => {
    alert('Thank you for your interest! We will contact you soon.');
    this.reset();
  })
  .catch(error => {
    alert('There was an error submitting your email. Please try again.');
  });
});

// No carousel animation needed for grid layout
