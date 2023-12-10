// Mapbox API
mapboxgl.accessToken = '';

const map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/outdoors-v12',
    center: cityCoordinates,
    zoom: 9,
});

fetch('/get_hotels_call')
    .then(response => response.json())
    .then(hotels_list1 => {
        console.log(hotels_list1);
        hotels_list1.forEach(hotel => {
            const popup = new mapboxgl.Popup({offset: 25}).setText(hotel['name'] + '\n' + hotel['address'])
            new mapboxgl.Marker({
                scale: 0.75
            })
                .setLngLat([hotel["co-ordinates"][0], hotel["co-ordinates"][1]])
                .setPopup(popup)
                .addTo(map);
        });
    });