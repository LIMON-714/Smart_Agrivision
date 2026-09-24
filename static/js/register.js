

    // ======================================
    // Show / Hide Password
    // ======================================

    function togglePassword(inputId, iconId) {

        const input = document.getElementById(inputId);
        const icon = document.getElementById(iconId);

        if (input.type === "password") {

            input.type = "text";

            icon.classList.remove("fa-eye");
            icon.classList.add("fa-eye-slash");

        }

        else {

            input.type = "password";

            icon.classList.remove("fa-eye-slash");
            icon.classList.add("fa-eye");

        }

    }


    // ======================================
    // Password Validation
    // ======================================

    const password = document.getElementById("password");
    const confirmPassword = document.getElementById("confirm_password");

    // Warning Div
    const passwordWarning = document.getElementById("password-warning");
    const confirmWarning = document.getElementById("confirm-warning");

    // Register Form
    const form = document.querySelector("form");


    // Password Length Check

    password.addEventListener("input", function () {

        if (password.value.length === 0) {

            passwordWarning.style.display = "none";

        }

        else if (password.value.length < 8) {

            passwordWarning.style.display = "block";

            passwordWarning.innerHTML =
                '<i class="fa-solid fa-circle-exclamation me-1"></i> Password must be at least 8 characters.';

            passwordWarning.className = "text-danger mt-2";

        }

        else {

            passwordWarning.style.display = "block";

            passwordWarning.innerHTML =
                '<i class="fa-solid fa-circle-check me-1"></i> Strong password.';

            passwordWarning.className = "text-success mt-2";

        }

    });


    // Confirm Password Check

    confirmPassword.addEventListener("input", function () {

        if (confirmPassword.value.length === 0) {

            confirmWarning.style.display = "none";

        }

        else if (password.value !== confirmPassword.value) {

            confirmWarning.style.display = "block";

            confirmWarning.innerHTML =
                '<i class="fa-solid fa-circle-xmark me-1"></i> Passwords do not match.';

            confirmWarning.className = "text-danger mt-2";

        }

        else {

            confirmWarning.style.display = "block";

            confirmWarning.innerHTML =
                '<i class="fa-solid fa-circle-check me-1"></i> Passwords matched.';

            confirmWarning.className = "text-success mt-2";

        }

    });


    // ======================================
    // Prevent Invalid Submit
    // ======================================

    form.addEventListener("submit", function (e) {

        if (password.value.length < 8) {

            e.preventDefault();

            password.focus();

            passwordWarning.style.display = "block";

            passwordWarning.innerHTML =
                '<i class="fa-solid fa-circle-exclamation me-1"></i> Password must contain at least 8 characters.';

            passwordWarning.className = "text-danger mt-2";

            return;

        }

        if (password.value !== confirmPassword.value) {

            e.preventDefault();

            confirmPassword.focus();

            confirmWarning.style.display = "block";

            confirmWarning.innerHTML =
                '<i class="fa-solid fa-circle-xmark me-1"></i> Passwords do not match.';

            confirmWarning.className = "text-danger mt-2";

            return;

        }

    });