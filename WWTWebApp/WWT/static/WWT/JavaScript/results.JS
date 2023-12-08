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
let currentDate = arrivalDT; //Starts at the arrival date

//Create the buttons loop
while (currentDate <= departureDT) {
    //console.log(currentDate.toLocaleDateString("en-US", { timeZone: "UTC" }));
    //Create the buttons
    newNode = document.createElement("button");
    newNode.classList.add("tablinks1");
    newNode.addEventListener("click", function (){selectDate(currentDate);});
    //newNode.addEventListener("click", showLocations()) Test 2nd
    innerText = document.createTextNode(currentDate.toLocaleDateString("en-US", { timeZone: "UTC" }));
    newNode.appendChild(innerText);

    currentSection.appendChild(newNode);

    //increment currentDate to the next day
    currentDate.setDate(currentDate.getDate() + 1);
}

//Generate the activity selector
//Reset and create the needed variables.
currentSelection = document.getElementById("resultsActivities"); //Gets the div element
newNode = null;
innerText = null;
const WWTActivities = ["1", "2", "3", "4", "5"]; //Array of activities, FIXME
let arrayLength = WWTActivities.length; //Holds the length of the activities array


//Create the buttons loop TESTME
for (let i = 0; i < arrayLength; i++) {
    //console.log(WWTActivities[i]);
    //Create the buttons
    newNode = document.createElement("button");
    newNode.classList.add("tabLinks2");
    newNode.addEventListener("click", function () { selectActivity(WWTActivities[i]); });
    //newNode.addEventListener("click", showLocations()) Test 2nd
    innerText = document.createTextNode(WWTActivities[i]);
    newNode.appendChild(innerText);

    currentSection.appendChild(newNode);
}