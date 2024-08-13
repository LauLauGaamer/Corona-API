document.getElementById('search-input').addEventListener('input', function() {
    const query = this.value;
    const resultsDiv = document.getElementById('search-results');

    if (query.length > 2) {
        fetch(window.location.href + `backend/live-search/?q=${query}`)
            .then(response => response.json())
            .then(data => {
                resultsDiv.innerHTML = '';

                if (data.towns.length > 0 || data.districts.length > 0 || data.states.length > 0) {
                    data.towns.forEach(function(town) {
                        const div = document.createElement('a');
                        div.classList.add('dropdown-item');
                        div.textContent = `${town.name} (PLZ: ${town.plz})`;
                        resultsDiv.appendChild(div);
                    });

                    data.districts.forEach(function(district) {
                        const div = document.createElement('a');
                        div.classList.add('dropdown-item');
                        div.textContent = "Landkreis: " + district.name;
                        resultsDiv.appendChild(div);
                    });

                    data.states.forEach(function(state) {
                        const div = document.createElement('a');
                        div.classList.add('dropdown-item');
                        div.textContent = "Bundesland: " + state.name;
                        resultsDiv.appendChild(div);
                    });

                    resultsDiv.style.display = 'block';
                } else {
                    resultsDiv.style.display = 'none';
                }
            });
    } else {
        resultsDiv.innerHTML = '';
        resultsDiv.style.display = 'none';
    }
});