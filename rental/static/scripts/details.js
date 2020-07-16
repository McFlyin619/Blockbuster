

function movieDetails() {

    var path = window.location.pathname;
    var pieces = path.split('/');
    var id = pieces[2];

    $.ajax({
        type: 'GET',
        url: '/api/movies/' + id,
        success: (movie) => {
            console.log(movie);
            $('h2').text(movie.title)
        },
        error: (err) => {
            console.log('Error: '+ err);
        }
    });
}


function init() {
    console.log('Details page loaded')
    movieDetails();
}

window.onload = init;