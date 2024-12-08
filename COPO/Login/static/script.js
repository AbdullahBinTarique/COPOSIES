
function togglePasswordVisibility() {
    const passwordInput = document.getElementById("password");
    const passwordType = passwordInput.getAttribute("type");

    if (passwordType === "password") {
        passwordInput.setAttribute("type", "text");
    } else {
        passwordInput.setAttribute("type", "password");
    }
}

document.getElementById("login-form").addEventListener("submit", function (event) {
    event.preventDefault();

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    if (validateEmail(email) && validatePassword(password)) {
        alert("Login successful!\nEmail: " + email);
    } else {
        alert("Invalid email or password. Please try again.");
    }
});

function validateEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

function validatePassword(password) {
    return password.length >= 6; 
}


