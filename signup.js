document.getElementById('signupForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    if (!validateEmail(email)) {
        alert('Invalid email format');
        return;
    }

    if (!validatePassword(password)) {
        alert('Password must be at least 6 characters long and contain at least one number');
        return;
    }

    localStorage.setItem('email', email);
    localStorage.setItem('password', password);
    alert('Signup successful! You can now log in.');
    window.location.href = "login.html"; // Redirect to login page
});

function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(String(email).toLowerCase());
}

function validatePassword(password) {
    const re = /^(?=.*\d)[a-zA-Z\d]{6,}$/;
    return re.test(String(password));
}
