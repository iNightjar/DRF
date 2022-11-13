const loginForm = document.getElementById("login-form");
const baseEndPoint = "http://localhost:8000/api/";

if (loginForm) {
    // handle this login form
    loginForm.addEventListener("submit", handleLogin);
}

function handleLogin(event) {
    console.log(event);
    event.preventDefault();
    const loginEndPoint = `${baseEndPoint}`;
    let loginFormData = new FormData(loginForm);
    let loginObjectData = Object.fromEntries(loginFormData);
    let bodyStr = JSON.stringify(loginObjectData);
    console.log(loginObjectData, bodyStr);

    const options = {
        method: "POST",
        Headers: {
            ContentType: "application/json",
        },
        body: bodyStr,
    };
    fetch(loginEndPoint, options) //  requets.POSTs , returning promise
        .then((response) => {
            // handle promise
            console.log(response);
            return response.json;
        })
        .then((x) => {
            console.log(x);
        })
        .catch((err) => {
            console.log("err", err);
        });
}
