from django.shortcuts import render
import airportsdata
import requests
import requests
import json

# Welcome page and input form
def index(request):
  return render(request, 'WWT/index.html')

# Results page
def results(request):
  try:
      #Attempt to read in information from the request
      #SEAN !!1
      #You have the destination and time, use that like a smart person!
      # Load the data into a dictionary with IATA as the key
      airports = airportsdata.load('IATA')

      # Define a function that takes a location as input and returns the IATA code
      def location_to_iata(city, state):
        # Loop through the airports dictionary
        for iata, airport in airports.items():
          # Check if the location is valid
          if city.lower() in (airport['city'].lower()) and state.lower() in (airport['subd'].lower()):
            # Return the IATA code
              return iata
        # If no match is found, return None
        return None

      print("Coming from?")
      city = input("Enter city: ")
      state = input("Enter state: ")

      print("Going to?")
      city1 = input("Enter city: ")
      state1 = input("Enter state: ")

      # Test the function with some examples
      print(location_to_iata('Jacksonville', 'Illinois')) # IJX
      print(location_to_iata('Jacksonville', 'florida')) # CRG
      print(location_to_iata('Jacksonville', 'New York')) # none

      origin = (location_to_iata("jacksonville", "florida"))
      dest = (location_to_iata("miami", "florida"))

      origin = (location_to_iata(city, state))
      dest = (location_to_iata(city1, state1))

      #origin = "IJX"
      #dest = "CRG"
      print("THE INPUTTED VALUES")
      print(origin)
      print(dest)


      origin = "EWR"
      dest = "JAX"
      #SIN, LHR

      url = 'https://partners.api.skyscanner.net/apiservices/v3/flights/live/search/create'
      headers = {'x-api-key': 'sh428739766321522266746152871799'}
      data = {
          "query": {
              "market": "UK",
              "locale": "en-GB",
              "currency": "USD",
              "query_legs": [{"origin_place_id": {"iata":origin}, "destination_place_id": {"iata":dest}, "date": {"year": 2023, "month": 12, "day": 12}}],
              "adults": 1,
              "cabin_class": "CABIN_CLASS_ECONOMY"
          }
      }

      response = requests.post(url, headers=headers, json=data)


      #==========================================

      # Check if the request was successful
      if response.status_code == 200:
          # Corrected line: Call response.json() as a method
          json_data = response.json()
          #print(json_data)
          # Iterate through all itineraries
          json_data["content"]["results"]["itineraries"]

          # Extract the "amount" field from the first pricing option  


        
          for itinerary_key, itinerary_data in json_data["content"]["results"]["itineraries"].items():
            amount = json_data["content"]["results"]["itineraries"][itinerary_key]["pricingOptions"][0]["price"]["amount"]
            amount_usd = round(float(amount) * 0.001, 2)
            dur = json_data["content"]["results"]["legs"][itinerary_key]["durationInMinutes"]
            dur_hr = (int(dur) / 60) #makes it hrs
            dur_min = (int(dur) % 60) #makes it mins
            name = json_data["content"]["results"]["agents"][itinerary_data["pricingOptions"][0]["agentIds"][0]]["name"]
            #print(f"For Itinerary {itinerary_key}, 
            print(f"A flight will be ${amount_usd} for {int((dur_hr))} hours and {int(dur_min)} minutes through {name}.")

      #name = name of the airline
      #amount_usd = amount of money for the flight in US dollars
      #dur_hr = duration of the flight's hours
      #dur_min = duration of the flight's minutes

      else:
        print(f"Error: {response.status_code}")
        print(response.text)

      #3rd page of the djangoproject.com > try tutorial> 3rd page > for loop in django 
      origin = request.GET["origin"]
      destination = request.GET["destination"]

      arrival = request.GET["arrival"]
      departure = request.GET["departure"]
  except (KeyError):
      #Information was missing from the request, redirect to index page
      return render(request, 'WWT/index.html', {"error_message": "Required information was missing for results."})
  else:
      #Information from the request was collected, direct to results page
      context = {"origin": origin, "destination": destination, "arrival": arrival, "departure": departure}
      return render(request, 'WWT/results.html', context)
  
# Location details page
def location(request, locationID):
  context = {"locationID": locationID}
  return render(request, 'WWT/location.html', context)

# About page
def about(request):
  return render(request, 'WWT/about.html')