document.addEventListener('DOMContentLoaded', () => {
    const cookieConsentBanner = document.getElementById('cookie-consent-banner');
    const acceptCookiesButton = document.getElementById('accept-cookies');
    const rejectCookiesButton = document.getElementById('reject-cookies');
    const consentCookieName = 'mrtrashcan_cookie_consent_accepted';

    // Function to set a cookie
    function setCookie(name, value, days) {
        const d = new Date();
        d.setTime(d.getTime() + (days * 24 * 60 * 60 * 1000));
        const expires = "expires=" + d.toUTCString();
        document.cookie = name + "=" + value + ";" + expires + ";path=/";
    }

    // Function to get a cookie
    function getCookie(name) {
        const cname = name + "=";
        const decodedCookie = decodeURIComponent(document.cookie);
        const ca = decodedCookie.split(';');
        for(let i = 0; i < ca.length; i++) {
            let c = ca[i];
            while (c.charAt(0) === ' ') {
                c = c.substring(1);
            }
            if (c.indexOf(cname) === 0) {
                return c.substring(cname.length, c.length);
            }
        }
        return "";
    }

    // Check if consent has already been given
    if (getCookie(consentCookieName) !== 'true') {
        cookieConsentBanner.style.display = 'block'; // Show the banner
    } else {
        window.dataLayer = window.dataLayer || [];
        function gtag() { dataLayer.push(arguments); }
        gtag('js', new Date());
        gtag('config', 'G-L0W78K0P0J');
    }
    
    // Event listener for accepting cookies
    acceptCookiesButton.addEventListener('click', () => {
        setCookie(consentCookieName, 'true', 30); // Set cookie for 30 days
        cookieConsentBanner.style.display = 'none'; // Hide the banner
    });
    rejectCookiesButton.addEventListener('click', () => {
        setCookie(consentCookieName, 'false', 5); // Set cookie for 5 days
        cookieConsentBanner.style.display = 'none'; // Hide the banner
    });
});
