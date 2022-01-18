
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

/**
 * If page title is Add Pension or Edit Pension, change scroll-behavior css property on root to auto.
 * Doing this because of bug on HTML 'required' form validation when scroll-behavior is smooth 
 * (happens on Add Pension or Edit Pension forms because of their length)
 */
function changeScrollToAuto() {
    if(document.title === "Add Pension" || document.title === "Edit Pension") {
        document.documentElement.style.setProperty('scroll-behavior', 'auto')
    }
}

/* initialise the Cancel btn on Sign Out form, Message Alerts, and page title check, when DOM loaded */
document.addEventListener("DOMContentLoaded", function () {
    initialiseGoBackButton();
    dismissAlert();
    changeScrollToAuto();
});