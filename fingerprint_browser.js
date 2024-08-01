(function() {
    var fingerprint = {
        userAgent: navigator.userAgent,
        platform: navigator.platform,
        language: navigator.language,
        screenResolution: screen.width + "x" + screen.height,
        colorDepth: screen.colorDepth,
        timezoneOffset: new Date().getTimezoneOffset(),
        plugins: Array.from(navigator.plugins).map(plugin => plugin.name),
        mimeTypes: Array.from(navigator.mimeTypes).map(mimeType => mimeType.type),
        cookiesEnabled: navigator.cookieEnabled,
        localStorage: typeof localStorage !== 'undefined',
        sessionStorage: typeof sessionStorage !== 'undefined',
        hardwareConcurrency: navigator.hardwareConcurrency,
        deviceMemory: navigator.deviceMemory
    };

    // Log the fingerprint data (for demonstration purposes)
    console.log('Browser Fingerprint:', fingerprint);

    // You might send this data to a server or store it
    // Example: sending to a server
    /*
    fetch('https://example.com/fingerprint', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(fingerprint)
    });
    */
})();
