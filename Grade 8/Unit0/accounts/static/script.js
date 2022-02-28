function verifyUsername(username) {
    let issues = "";

    // make sure there are only a-z and 0-9 in username
    let regex = /^[a-z0-9]+$/i;
    if (!regex.test(username)) {
        issues += " - Username must only contain a-z and 0-9.\n";
    }

    // Username length stuff
    if (username.length < 3) {
        issues += " - Username must be at least 3 characters long.\n";
    }
    if (username.length > 20) {
        issues += " - Username must be less than 20 characters long.\n";
    }

    // Returning stuff
    if (issues.length > 0) {
        return issues;
    } else {
        return false;
    }
}

function verifyPasswords(password, password2) {
    let issues = "";

    // pwd comparison
    if (password != password2) {
        issues += " - Passwords do not match.\n";
    }

    // pwd length
    if (password.length < 8) {
        issues += " - Password must be at least 8 characters long.\n";
    }

    // Pwd must contain uppercase letter, lowercase letter, number, and special character
    let uppercase = false;
    let lowercase = false;
    let number = false;
    let special = false;

    // Pretty sure this all works using ascii but im not sure
    // Since i kinda just let copilot do its thing
    for (let i = 0; i < password.length; i++) {
        // Check for special character
        if ((password.charCodeAt(i) >= 33 && password.charCodeAt(i) <= 47) || (password.charCodeAt(i) >= 58 && password.charCodeAt(i) <= 64)){ special = true; }

        // Check for number
        if (password.charCodeAt(i) >= 48 && password.charCodeAt(i) <= 57) { number = true; }

        // Check for lowercase letter
        if (password.charCodeAt(i) >= 97 && password.charCodeAt(i) <= 122) { lowercase = true; }

        // Check for uppercase letter
        if (password.charCodeAt(i) >= 65 && password.charCodeAt(i) <= 90) { uppercase = true; }
    }

    // If any remaining falses add it to issues string
    if (!uppercase) { issues += " - Password must contain at least one uppercase letter.\n"; }
    if (!lowercase) { issues += " - Password must contain at least one lowercase letter.\n"; }
    if (!number) { issues += " - Password must contain at least one number.\n";}
    if (!special) { issues += " - Password must contain at least one special character.\n"; }

    // Returning stuff
    if (issues.length > 0) {
        return issues;
    } else {
        return false;
    }
}

function verifyReg() {
    const registrationForm = document.getElementById('register');
    let formData = new FormData(registrationForm);

    // Getting data from forms
    let username = formData.get('username')
    let password1 = formData.get('password1')
    let password2 = formData.get('password2')
    let issues = "Your registration has the following issues: \n"; // Length is 45

    // Username verif
    let userNameVerif = verifyUsername(username);
    if (userNameVerif) {
        issues += userNameVerif;
    }

    // pwd verifs
    let pwdsVerif = verifyPasswords(password1, password2);
    if (pwdsVerif) {
        issues += pwdsVerif;
    }

    // If there are no issues, submit the form
    if (issues.length == 45) {
        return true;
    } else {
        issues += "Now go fix these issues or else.";
        alert(issues);
        return false;
    }

}
