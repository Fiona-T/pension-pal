
/**
 * If Cancel btn element on Sign Out form exists, add event listener, when clicked
 * go back to previous page in window history
 */
function initialiseGoBackButton() {
    if(document.getElementById("go-back")){
        document.getElementById("go-back").addEventListener("click", function () {
            history.back();
            return false;
        });
    }
}

/**
 * If msg alert element exists, set timeout so it closes itself if user doesn't close it
 */
function dismissAlert() {
    if(document.getElementById("msg")){
        setTimeout(() => {
            let message = document.getElementById("msg")
            let alert = new bootstrap.Alert(message);
            alert.close();
        }, 3000);
    }
}

/* initialise the Cancel btn on Sign Out form, and Message Alerts when DOM loaded */
document.addEventListener("DOMContentLoaded", function () {
    initialiseGoBackButton();
    dismissAlert();
});