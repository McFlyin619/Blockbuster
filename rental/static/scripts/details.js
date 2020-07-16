

function movieDetails() {

    var path = window.location.pathname;
    var pieces = path.split('/');
    var id = pieces[2];

    $.ajax({
        type: 'GET',
        url: '/api/movies/' + id,
        success: (movie) => {
            console.log(movie);
            $('h1').text(movie.title);
            detailsDisplay(movie);
        },
        error: (err) => {
            console.log('Error: '+ err);
        }
    });
}

function detailsDisplay(movie) {
    var display = `
    <div class="jumbotron jumbotron-fluid">
        <div class="container">
            <h1 class="display-4">${movie.title}</h1>
            <p class="lead">${movie.title} is a ${movie.genre.name} movie that was released in ${movie.release_year} and is ${movie.length_min} minutes long. We have ${movie.in_stock} in stock!</p>
            <button class="btn btn-outline-primary btn-block">Rent ${movie.title} for only $${movie.price}</button>
        </div>
    </div>
    `;
    $('.movie-details').append(display);
}


function init() {
    console.log('Details page loaded')
    movieDetails();
}

window.onload = init;