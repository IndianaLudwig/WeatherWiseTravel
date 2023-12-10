// Mapbox API
mapboxgl.accessToken = '';

const map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/outdoors-v12',
    center: cityCoordinates,
    zoom: 9,
});

fetch('/get_locations_call')
    .then(response => response.json())
    .then(locations_list => {
        console.log(locations_list);
        locations_list.forEach(location => {
            const popup = new mapboxgl.Popup({offset: 25}).setText(location['name'] + '\n' + location['address'])
            new mapboxgl.Marker({
                scale: 0.75
            })
                .setLngLat([location["co-ordinates"][0], location["co-ordinates"][1]])
                .setPopup(popup)
                .addTo(map);
        });
    });