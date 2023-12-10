// Mapbox API
mapboxgl.accessToken = '';

const map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/outdoors-v12',
    center: cityCoordinates,
    zoom: 9,
});

fetch('/get_location_info')
    .then(response => response.json())
    .then(location_info => {
        console.log(location_info);
        location_info.forEach(info => {
            const popup = new mapboxgl.Popup({ offset: 25 }).setText(info['name'] + '\n' + info['address'])
            new mapboxgl.Marker({
                scale: 0.75
            })
                .setLngLat([info["co-ordinates"][0], info["co-ordinates"][1]])
                .setPopup(popup)
                .addTo(map);
            // Add details to the table
            addToDetailsTable(info);
        });
    });

// Function to add details to the table
function addToDetailsTable(info) {
    const detailsTableBody = document.getElementById('details-body');
    const row = detailsTableBody.insertRow();
    const nameCell = row.insertCell(0);
    const addressCell = row.insertCell(1);
    const ratingCell = row.insertCell(2);
    const linkCell = row.insertCell(3);

    nameCell.textContent = info['name'];
    addressCell.textContent = info['address'];
    ratingCell.textContent = info['rating'];
    linkCell.innerHTML = `<a href="${info['link']}" target="_blank">Link</a>`;
}