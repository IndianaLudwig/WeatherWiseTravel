//Page creation
//Create page display variables
let daySelection = null;
let activitySelection = null;

//Obtain the HTML query string
const queryString = window.location.search;
//console.log(queryString);

//Parse the parameters
const urlParameters = new URLSearchParams(queryString);

//Convert the arrival and departure dates to the date data type
const arrivalDT = new Date(urlParameters.get('arrival'));
const departureDT = new Date(urlParameters.get('departure'));

//Correctly getting the dates to display
//arrivalDT.toLocaleDateString("en-US", { timeZone: "UTC" });
//departureDT.toLocaleDateString("en-US", { timeZone: "UTC" });

//Generating title
document.getElementById("resultsTitle").innerHTML = 
    "Results for " + urlParameters.get('destination') + " from " +
    arrivalDT.toLocaleDateString("en-US", { timeZone: "UTC" }) + " to " +
    departureDT.toLocaleDateString("en-US", { timeZone: "UTC" });

//Generate the day selector
//Create needed variables.
let currentSection = document.getElementById("resultsDays"); //Gets the div element
let newNode = null;
let innerText = null;
let currentDate = new Date(urlParameters.get('arrival')); //Starts at the arrival date

//Create the buttons loop FIXME, error present
while (currentDate <= departureDT) {
    //console.log(currentDate.toLocaleDateString("en-US", { timeZone: "UTC" }));
    //Create the buttons
    newNode = document.createElement("button");
    newNode.classList.add("tabLinks1");
    newNode.setAttribute('id', currentDate.toLocaleDateString("en-US", { timeZone: "UTC" }));
    newNode.addEventListener("click", function () { selectDate(currentDateString); });
    newNode.addEventListener("click", showLocations());
    innerText = document.createTextNode(currentDate.toLocaleDateString("en-US", { timeZone: "UTC" }));
    newNode.appendChild(innerText);

    currentSection.appendChild(newNode);

    //increment currentDate to the next day
    currentDate.setDate(currentDate.getDate() + 1);
}

//Generate the activity selector
//Reset and create the needed variables.
currentSection = document.getElementById("resultsActivities"); //Gets the div element
newNode = null;
innerText = null;
const WWTActivities = ["1", "2", "3", "4", "5"]; //Array of activities, FIXME
let arrayLength = WWTActivities.length; //Holds the length of the activities array

//Create the buttons loop
for (let i = 0; i < arrayLength; i++) {
    //console.log(WWTActivities[i]);
    //Create the buttons
    newNode = document.createElement("button");
    newNode.classList.add("tabLinks2");
    newNode.addEventListener("click", function () { selectActivity(WWTActivities[i]); });
    newNode.addEventListener("click", showLocations());
    innerText = document.createTextNode(WWTActivities[i]);
    newNode.appendChild(innerText);

    currentSection.appendChild(newNode);
}

//Functions
//Function to get the day selection and update tabs FIXME
function selectDate(chosenDate) {
    //Create variables
    let i = null;
    let tabLinks = null;

    //Get the day selection
    daySelection = chosenDate;
    console.log(chosenDate)
    //Update the tabs tabLinks1
    //Remove the activeTab class from all tabLinks1
}

//Function to get the activity selection and update tabs
function selectActivity(chosenActivity) {
    //Create variables
    let i = null;
    let tabLinks = null;

    //Get the activity selection
    activitySelection = chosenActivity;

    //Update the tabs tabLinks2
    //Remove the activeTab class from all tabLinks2
}

//Function to display locations for the activity and date FIXME
function showLocations() {
    //Check if both a day and activity are selected
    if ((daySelection != null) && (activitySelection != null)) {
        //Update the location selector
        console.log("daySelection = " + daySelection + "\nactivitySelection = " + activitySelection);
    }
}