//Mapbox API
mapboxgl.accessToken = '';

const map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/outdoors-v12',
    center: cityCoordinates,
    zoom: 9,
});

fetch('/get_car_rentals')
    .then(response => response.json())
    .then(car_rentals_list => {
        console.log(car_rentals_list);
        car_rentals_list.forEach(hotel => {
            const popup = new mapboxgl.Popup({offset: 25}).setText(hotel['name'] + '/n' + hotel['address'])
            new mapboxgl.Marker({
                scale: 0.75
            })
                .setLngLat([hotel["co-ordinates"][0], hotel["co-ordinates"][1]])
                .setPopup(popup)
                .addTo(map);
        });
    });