import requests
#api key: sh428739766321522266746152871799

import requests
import json

url = 'https://partners.api.skyscanner.net/apiservices/v3/flights/live/search/create'
headers = {'x-api-key': 'sh428739766321522266746152871799'}
data = {
    "query": {
        "market": "UK",
        "locale": "en-GB",
        "currency": "USD",
        "query_legs": [{"origin_place_id": {"iata": "LHR"}, "destination_place_id": {"iata": "SIN"}, "date": {"year": 2023, "month": 12, "day": 22}}],
        "adults": 1,
        "cabin_class": "CABIN_CLASS_ECONOMY"
    }
}

response = requests.post(url, headers=headers, json=data)

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
    

        #name = json_data["content"]["results"]["places"][itinerary_key]["name"]


        # Iterate through all pricing options for each itinerary
#        for pricing_option in itinerary_data.get("pricingOptions", []):
 #           # Extract the "amount" and "name" fields from each pricing option
  #          amount = pricing_option.get("price", {}).get("amount", "Amount not available")
#
 #           name = pricing_option.get("items", [{}])[0].get("agents", "Name not available")

  #          print(f"  Amount: {amount_usd}, Name: {name}")


  '''url = 'https://partners.api.skyscanner.net/apiservices/v3/flights/indicative/search'
  headers = {'x-api-key': 'sh428739766321522266746152871799'}
  data = {
      "query": {
          "market": "UK",
          "locale": "en-GB",
          "currency": "GBP",
          "queryLegs": [{
              "originPlace": {
                  "queryPlace": {
                      "iata": "LHR"
                  }
              },
              "destinationPlace": {
                  "queryPlace": {
                      "iata": "LAX"
                  }
              },
              "anytime": True
          }]
      }
  }

  response = requests.post(url, headers=headers, json=data)
  print(response.json())

  #for flight in response.json()["flights"]:
   # print(flight["price"])
  '''

  '''
  import requests

  url = 'https://partners.api.skyscanner.net/apiservices/v3/flights/live/search/create'
  headers = {'x-api-key': 'sh428739766321522266746152871799'}
  data = {
      "query": {
          "market": "UK",
          "locale": "en-GB",
          "currency": "USD",
          "query_legs": [{"origin_place_id": {"iata": "LHR"}, "destination_place_id": {"iata": "SIN"}, "date": {"year": 2023, "month": 12, "day": 22}}],
          "adults": 1,
          "cabin_class": "CABIN_CLASS_ECONOMY"
      }
  }

  response = requests.post(url, headers=headers, json=data)

  # Check if the request was successful
  if response.status_code == 200:
      # Corrected line: Call response.json() as a method
      json_data = response.json()
      # Extract the "amount" field from the first pricing option
  # Extract the "amount" field from the first pricing option
      amount = json_data["content"]["results"]["itineraries"]["13554-2312220910--31876-0-16292-2312230605"]["pricingOptions"][0]["price"]["amount"]
      print(f"Amount: {amount}")
      amount = json_data["content"]["results"]["itineraries"]["13554-2312220910--31876-0-16292-2312230605"]["pricingOptions"][0]["price"]["amount"]
      print(f"Amount: {amount}")
      #for pricing_option in json_data["content"]["results"]["itineraries"]["13554-2312220910--31876-0-16292-2312230605"]["pricingOptions"]:
      #  amount = pricing_option["price"]["amount"]
      #  print(f"Amount: {amount}")
  else:
      print(f"Error: {response.status_code}")
      print(response.text)
  #print(f"The cheapest flight is ${data['Itineraries'][0]['PricingOptions'][0]['Price']}")
  '''



'''
import requests

url = 'https://partners.api.skyscanner.net/apiservices/v3/flights/live/search/create'
headers = {'x-api-key': 'sh428739766321522266746152871799'}
data = {
    "query": {
        "market": "UK",
        "locale": "en-GB",
        "currency": "USD",
        "query_legs": [{"origin_place_id": {"iata": "LHR"}, "destination_place_id": {"iata": "SIN"}, "date": {"year": 2023, "month": 12, "day": 22}}],
        "adults": 1,
        "cabin_class": "CABIN_CLASS_ECONOMY"
    }
}

response = requests.post(url, headers=headers, json=data)

# Check if the request was successful
if response.status_code == 200:
    # Corrected line: Call response.json() as a method
    json_data = response.json()

    pricing_option = json_data["content"]['results']['itineraries']['13554-2312220910--31876-0-16292-2312230605']['pricingOptions'][0]
    amount = pricing_option['price']['amount']
    name = pricing_option['items'][0]['agentId']

    print(f"Amount: {amount}, Name: {name}")

    # Iterate through all itineraries
#    for itinerary_key, itinerary_data in json_data["content"]["results"]["itineraries"].items():
 #       # Iterate through all pricing options for each itinerary
  #      for pricing_option in itinerary_data.get("pricingOptions", []):
   #         # Extract the "amount" field from each pricing option
    #        amount = pricing_option.get("price", {}).get("amount", "Amount not available")
     #       amount_usd = round(float(amount)*.001, 2)
      #      print(f"For Itinerary {itinerary_key}")
       #      print(f"Price {amount_usd}")

else:
    print(f"Error: {response.status_code}")
    print(response.text)
    

import requests
import json

# Replace with your own API key
api_key = "skyscanner_api_key"

# Create a session
session_url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/pricing/v1.0"
session_headers = {
    "x-rapidapi-key": api_key,
    "x-rapidapi-host": "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
    "content-type": "application/x-www-form-urlencoded"
}
session_data = {
    "inboundDate": "",
    "cabinClass": "economy",
    "children": 0,
    "infants": 0,
    "country": "UK",
    "currency": "GBP",
    "locale": "en-GB",
    "originPlace": "LHR-sky",
    "destinationPlace": "CDG-sky",
    "outboundDate": "2023-11-30",
    "adults": 1
}
session_response = requests.post(session_url, headers=session_headers, data=session_data)
session_id = session_response.headers["Location"].split("/")[-1]

# Poll the results
poll_url = f"https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/pricing/uk1/v1.0/{session_id}"
poll_headers = {
    "x-rapidapi-key": "sh428739766321522266746152871799",
    "x-rapidapi-host": "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
}
poll_params = {
    "pageIndex": 0,
    "pageSize": 10
}
poll_response = requests.get(poll_url, headers=poll_headers, params=poll_params)
poll_data = poll_response.json()

# Print the price and name of airport
for itinerary in poll_data["Itineraries"]:
    price = itinerary["PricingOptions"][0]["Price"]
    outbound_leg_id = itinerary["OutboundLegId"]
    for leg in poll_data["Legs"]:
        if leg["Id"] == outbound_leg_id:
            origin_id = leg["OriginStation"]
            destination_id = leg["DestinationStation"]
            for place in poll_data["Places"]:
                if place["Id"] == origin_id:
                    origin_name = place["Name"]
                if place["Id"] == destination_id:
                    destination_name = place["Name"]
    print(f"Price: {price} GBP")
    print(f"Origin: {origin_name}")
    print(f"Destination: {destination_name}")
    print()
'''