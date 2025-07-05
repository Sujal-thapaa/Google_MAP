// Check if page is loaded in iframe and hide search bar for small minimap
window.addEventListener('DOMContentLoaded', function() {
    if (window.self !== window.top) {
        // Page is in an iframe (small minimap)
        document.body.classList.add('in-iframe');
    }
});

// Toggle points visibility when map is clicked
function togglePoints() {
    const mapContainer = document.getElementById('map-container');
    mapContainer.classList.toggle('show-points');
}

// Redirect to the respective Street View location in index.html
function redirectToStreetView(locationKey) {
    sessionStorage.setItem("selectedLocation", locationKey);
    window.location.href = "index.html";
}

// Listen for messages from parent window to glow buildings
window.addEventListener('message', function(event) {
    if (event.data.type === 'glowBuilding') {
        glowBuilding(event.data.locationKey);
    }
});

// Function to make a building glow
function glowBuilding(locationKey) {
    // First, remove glow from all points
    const allPoints = document.querySelectorAll('.point');
    allPoints.forEach(point => {
        point.classList.remove('glow');
    });

    // Then add glow to the selected building
    const selectedPoint = document.querySelector(`[data-location="${locationKey}"]`);
    if (selectedPoint) {
        selectedPoint.classList.add('glow');
        // Show all points so the glow is visible
        document.getElementById('map-container').classList.add('show-points');
        
        // Remove glow after 5 seconds
        setTimeout(() => {
            selectedPoint.classList.remove('glow');
        }, 5000);
    }
}

// Building search functionality for open minimap
const openBuildingList = [
    { key: 'library', name: 'University Library' },
    { key: 'madisonHall', name: 'Madison Hall' },
    { key: 'sandelHall', name: 'Sandel Hall' },
    { key: 'GeorgeTWalkerHall', name: 'George T. Walker Hall' },
    { key: 'footbridge', name: 'Footbridge' },
    { key: 'hub', name: 'The Hub' },
    { key: 'schulzeDiningHall', name: 'Schulze Dining Hall' },
    { key: 'coliseum', name: 'Fant-Ewing Coliseum' },
    { key: 'studentSuccessCenter', name: 'Student Success Center' },
    { key: 'UniversityCommons', name: 'University Commons' },
    { key: 'UniversitySuites', name: 'University Suites' },
    { key: 'cnsb', name: 'Chemistry & Natural Science Building' },
    { key: 'bcm', name: 'BCM Building' },
    { key: 'KittyDeGreeHall', name: 'Kitty DeGree Hall' },
    { key: 'SugarHall', name: 'Sugar Hall' },
    { key: 'HemphillHall', name: 'Hemphill Hall' },
    { key: 'CoenenHall', name: 'Coenen Hall' },
    { key: 'StraussHall', name: 'Strauss Hall' },
    { key: 'HannaHall', name: 'Hanna Hall' }
];

function showOpenSearchDropdown() {
    const dropdown = document.getElementById('open-search-dropdown');
    populateOpenDropdown(openBuildingList);
    dropdown.style.display = 'block';
    
    // Show all points when search is focused (since this is full map view)
    document.getElementById('map-container').classList.add('show-points');
}

function hideOpenSearchDropdown() {
    // Add a small delay to allow for option clicks
    setTimeout(() => {
        const dropdown = document.getElementById('open-search-dropdown');
        dropdown.style.display = 'none';
    }, 150);
}

function filterOpenBuildings(searchText) {
    const filtered = openBuildingList.filter(building =>
        building.name.toLowerCase().includes(searchText.toLowerCase())
    );
    populateOpenDropdown(filtered);
}

function populateOpenDropdown(buildings) {
    const dropdown = document.getElementById('open-search-dropdown');
    dropdown.innerHTML = '';
    
    buildings.forEach(building => {
        const option = document.createElement('div');
        option.className = 'open-search-option';
        option.textContent = building.name;
        option.onclick = () => selectOpenBuilding(building.key, building.name);
        dropdown.appendChild(option);
    });
}

function selectOpenBuilding(locationKey, buildingName) {
    // Show all points first since this is the full map view
    document.getElementById('map-container').classList.add('show-points');
    
    // Glow the selected building
    glowBuilding(locationKey);
    
    // Update search input
    document.getElementById('open-building-search').value = buildingName;
    document.getElementById('open-search-dropdown').style.display = 'none';
    
    // Clear the search after a short delay
    setTimeout(() => {
        document.getElementById('open-building-search').value = '';
    }, 3000);
} 