

function fetchCatalog() {
    $.ajax({
        type: 'GET',
        url: '/api/movies',
        success: (res) => {
            console.log(res);
            for(let i=0; i<res.objects.length; i++) {
                var movie = res.objects[i];
                displayMovie(movie);
            }
        },
        error: (err) => {
            console.log("Error: " + err);
        }
    });
}

function displayMovie(movie) {
    var template = `
        <div class="card" style="width: 25rem;">
            <img src="${movie.image_url}" class="card-img-top" alt="...">
            <div class="card-body">
                <h2 class="card-title">${movie.title} - $${movie.price.toFixed(2)}</h2>
                <h4>${movie.genre.name}</h4>
                <p class="card-text"><b>Released:</b> ${movie.release_year}</p>
                <p class="card-text"><b>Length:</b> ${movie.length_min} min</p>
                <a href="/details/${movie.id}" class="btn btn-primary">Info</a>
            </div>
        </div>
    `;

    var container = $('.catalog-container')
    container.append(template);
}




function init() {
    console.log('Catalog page loaded');

    fetchCatalog()
}

window.onload = init;

