document.getElementById('search-button').addEventListener('click', function() {
    const query = document.getElementById('search-input').value.trim();
    
    if (query) {
        const encodedQuery = encodeURIComponent(query);
        const newUrl = `search/?q=${encodedQuery}`;
        window.location.href = newUrl;
    } else {
        alert('Bitte geben Sie einen Suchbegriff ein.');
    }
});