import datetime
from datetime import date
from datetime import timedelta
import django #Used for connecting back and front end code
import flask  #Used for geocoding maps
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

def parse_places_nearby(place_results) :
    if(place_results['status'] == 'OK') :
        for place in place_results['results']:
            my_place_id = place['place_id']
            my_place_name = place['name']
            my_place_address = place['formatted_address']
            my_place_status = place['business_status']
            print(my_place_name)
            print("\t Address : " + my_place_address)
            print("\t id :" + my_place_id)
                
    else :
        print("Error in API callback result")

daymonth = input("Enter the month: " )
daydate = input("Enter the date: ")
start_day = datetime.date(2023, int(daymonth), int(daydate))
daymonth = input("Enter the end month: " )
daydate = input("Enter the end date: ")
end_day = datetime.date(2023, int(daymonth), int(daydate))
Location = input("Enter the Destination: ")
activity = input("Enter the activity: ")
# Google Places API
API_KEY = ""
gmaps = googlemaps.Client(key = API_KEY)
geolocator = geopy.geocoders.Nominatim(user_agent="MyApp")


Outdoorweather = ["Overcast", "Partially Cloudy", "Sunny", "Pleasent"]
geo_location = geolocator.geocode(Location)
my_location = [geo_location.latitude,geo_location.longitude]
if debug :
    print(geo_location)
    print(my_location)

today = date.today()
range1 = end_day - start_day
range1 = str(range1)
range1 = range1.split()[0]
range1 = int(range1) + 1
threshold = today + timedelta(days=14)
current_day = start_day

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
if (end_day > threshold):
    print("Invalid dates")
else:    
    for i in range(15):
        day = (x['days'][i]['datetime'])
        if(str(current_day) == str(day)):
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
            my_place_results = gmaps.places(query = activity ,location = my_location, radius = 50000, type = 'tourist_attraction')
            parse_places_nearby(my_place_results)
            print("\n" + "On " + str(current_day) + ", " + resolvedaddrress + ": " + "\n" + "Temperature: " + str(temperature) + '\n' + 
                'Precipitation: ' + str(precipitation) + '%' + '\n' + 'Weather condition: ' + str(weather_condition) + '\n' + 'Cloud cover: ' + str(cloudcover))
            if weather_condition not in Outdoorweather:
                print("We suggest indoor activities due to weather conditions")
                my_place_results = gmaps.places(query = "Indoor tourist attractions" ,location = my_location, radius = 50000, type = 'tourist_attraction')
                parse_places_nearby(my_place_results)
            if debug :
                pprint.pprint(my_place_results)


            if (current_day < end_day):
                current_day = current_day + timedelta(days=1)


            

                


