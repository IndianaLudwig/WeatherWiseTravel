# pip install googlemaps
# pip install prettyprint
# pip install xlsxwriter
# pip install geopy

import datetime
from datetime import date
from datetime import timedelta
from flask import Flask, render_template, jsonify
import django #Used for connecting back and front end code
import json   #Used for weather reading
import pprint
import requests 
import googlemaps
import time
import json
import xlsxwriter
import geopy
from geopy.geocoders import Nominatim
debug = 0
locations_list= []

def parse_places_nearby(place_results) :
    if(place_results['status'] == 'OK') :
        for place in place_results['results']:
            my_place_id = place['place_id']
            my_place_name = place['name']
            my_place_address = place['formatted_address']
            my_place_lat = place['geometry']['location']['lat']
            my_place_lng = place['geometry']['location']['lng']
            thisdict = {
                    "name": my_place_name,
                    "address": my_place_address,
                    "co-ordinates": [my_place_lng, my_place_lat]
                }
            locations_list.append(thisdict)
            #my_fields = ['name', 'formatted_phone_number','type']
            #place_details = gmaps.place(place_id = my_place_id, fields = my_fields)
            #if(my_place_status=='OPERATIONAL'):
            
                
    else :
        print("Error in API callback result")

daymonth = input("Enter the month: " )
daydate = input("Enter the date: ")
actual_day = datetime.date(2023, int(daymonth), int(daydate))
Location = input("Enter the Destination: ")
activity = input("Enter the activity: ")
# Google Places API
API_KEY = ""
gmaps = googlemaps.Client(key = API_KEY)
geolocator = geopy.geocoders.Nominatim(user_agent="MyApp")
Outdoorweather = ["Overcast", "Partially Cloudy", "Sunny", "Pleasent"]
geo_location = geolocator.geocode(Location)
my_location = [geo_location.latitude,geo_location.longitude]
city_coordinates = [geo_location.longitude,geo_location.latitude]
if debug :
    print(geo_location)
    print(my_location)

today = date.today()
threshold = today + timedelta(days=14)
#range1 = end_day - start_day
#range1 = str(range1)
#range1 = range1.split()[0]
#range1 = int(range1) + 1
#current_day = actual_day



BaseURL = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'

ApiKey='WPFBLWYENQY3G3RMLQPX9L9DX'
#UnitGroup sets the units of the output - us or metric
UnitGroup='us'

#basic query including location
ApiQuery=BaseURL + Location

#Url is completed. Now add query parameters (could be passed as GET or POST)
ApiQuery+="?"

#append each parameter as necessary
ApiQuery+="&unitGroup="+UnitGroup

ApiQuery+="&key="+ApiKey
#print(' - Running query URL: ', ApiQuery)
response = requests.get(ApiQuery)
x = response.json()
if (actual_day > threshold):
    print("Invalid dates")
else:    
    for i in range(15):
        day = (x['days'][i]['datetime'])
        if(str(actual_day) == str(day)):
            description = str(x['days'][i]['description'])
            #this givs the autocorrected address
            resolvedaddrress = str(x['resolvedAddress'])
            #this is chance of rain
            precip = (x['days'][i]['precipprob'])
            #additional experimentation
            icon = str(x['days'][i]['icon'])
            precipitation = str(x['days'][i]['precip'])
            conditions = str(x['days'][i]['conditions']).lower()
            temperature = (x['days'][i]['temp'])
            precipitation = (x['days'][i]['precip'])
            windspeed = (x['days'][i]['windspeed'])
            cloudcover = (x['days'][i]['cloudcover'])
            humidity = (x['days'][i]['humidity'])
            uvindex = (x['days'][i]['uvindex'])
            snow = (x['days'][i]['snow'])
            #print(x)

            # Initialize the weather condition
            weather_condition = "Unknown"

            #Wind Condition
            if windspeed > 50:
                weather_condition = "Extremely Windy"

            #Rainy weather
            elif "rain" in conditions or precipitation >= 1.0:
                if temperature < 32 and humidity > 70:
                    weather_condition = "Cold and Rainy"
                else:
                    weather_condition = "Rainy"

            #Snowy weather
            elif "snow" in conditions or snow > 0.0:
                if temperature < 32 and windspeed > 20:
                    weather_condition = "Cold Snowy and Windy"
                elif temperature < 32:
                    weather_condition = "Cold and Snowy"
                else:
                    weather_condition = "Snowy"

            #Cloudy weather
            elif cloudcover > 80 and temperature < 32:
                weather_condition = "Overcast and Cold"
            elif cloudcover > 80:
                weather_condition = "Overcast"
            elif cloudcover > 40:
                if temperature < 32:
                    weather_condition = "Partialy Cloudy and Cold"
                else:
                    weather_condition = "Partially Cloudy"
            elif temperature < 32 and windspeed > 20:
                weather_condition = "Cold and Windy"

            #Sunny weather
            elif temperature > 90 :
                if humidity > 70 :
                    if uvindex > 7:
                        weather_condition = "Extremely Hot and High UV Index"
                    else:
                        weather_condition = "Extremely Hot"
                elif uvindex > 5:
                    weather_condition = "Extremely Hot with Moderate UV Index"
                else :
                    weather_condition = "Sunny"
            elif temperature < 32 :
                if humidity > 70:
                    weather_condition = "Cold and Humid"
                elif uvindex > 7:
                    weather_condition = "Cold with High UV Index"
                else :
                    weather_condition = "Cold"
            else :
                weather_condition = "Pleasent"

            #################################################################################################
            #print("\n" + "On " + str(day) + ",\n" + resolvedaddrress + ": " "\n" + description + "\n" + "Chance of rain: " + str(precipitation) + "%" + "\n" + "Conditions: " + conditions + "\n" + "Units: " + UnitGroup + "\n" + "Icon: " + icon)
            #print("Today's Weather: " + weather_condition)
#weather_condition = "Sunny"
if weather_condition in Outdoorweather:
    my_place_results = gmaps.places(query = activity ,location = my_location, radius = 50000, type = 'tourist_attraction')
    parse_places_nearby(my_place_results)
    
else:                
    my_place_results = gmaps.places(query = "Indoor tourist attractions" ,location = my_location, radius = 50000, type = 'tourist_attraction')
    parse_places_nearby(my_place_results)
if debug :
    pprint.pprint(my_place_results)

###################################################################################################

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', city_coordinates=city_coordinates)

@app.route('/get_locations_call', methods=['GET'])
def get_locations_call():
    return jsonify(locations_list)

if __name__ == '__main__':
    app.run(debug=True)