function search(query){
    const resultsDiv = document.getElementById('search-results');

    if (query.length > 1) {
        fetch(window.location.href + `backend/live-search/?q=${query}`)
            .then(response => response.json())
            .then(data => {
                resultsDiv.innerHTML = '';

                if (data.towns.length > 0 || data.districts.length > 0 || data.states.length > 0) {
                    data.towns.forEach(function(town) {
                        const div = document.createElement('a');
                        div.classList.add('dropdown-item');
                        div.textContent = `${town.name} (PLZ: ${town.plz})`;
                        div.setAttribute("href", 'http://127.0.0.1:8000/corona/search/?q=' + query)
                        resultsDiv.appendChild(div);
                    });

                    data.districts.forEach(function(district) {
                        const div = document.createElement('a');
                        div.classList.add('dropdown-item');
                        div.textContent = "Landkreis: " + district.name;
                        div.setAttribute("href", 'http://127.0.0.1:8000/corona/search/?q=' + query)
                        resultsDiv.appendChild(div);
                    });

                    data.states.forEach(function(state) {
                        const div = document.createElement('a');
                        div.classList.add('dropdown-item');
                        div.textContent = "Bundesland: " + state.name;
                        div.setAttribute("href", 'http://127.0.0.1:8000/corona/search/?q=' + query)
                        resultsDiv.appendChild(div);
                    });

                    if(!data.querySucceeded){
                        const div = document.createElement('div');
                        div.classList.add('dropdown-item');
                        div.textContent = "Weitere Ergebnisse ..";
                        resultsDiv.appendChild(div);
                    }

                    resultsDiv.style.display = 'block';
                } else {
                    resultsDiv.style.display = 'none';
                }
            });
    } else {
        resultsDiv.innerHTML = '';
        resultsDiv.style.display = 'none';
    }
}

document.getElementById('search-input').addEventListener('input', function() {
    const query = this.value;
    search(query);
});

document.getElementById('search-input').addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault();
        window.location.href = window.location.href + 'search/?q=' + this.value; //geht noch nicht
    }
});