
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

/* initialise the Cancel btn on Sign Out form, when DOM loaded */
document.addEventListener("DOMContentLoaded", function () {
    initialiseGoBackButton();
});