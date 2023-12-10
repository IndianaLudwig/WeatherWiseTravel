# pip install googlemaps
# pip install prettyprint
# pip install xlsxwriter
# pip install geopy

from flask import Flask, render_template, jsonify
import googlemaps
import pprint
import time
import json
import xlsxwriter
import geopy

from geopy.geocoders import Nominatim
debug = 0
hotels_list= []


def lat_long(place_results) :
    if(place_results['status'] == 'OK') :      
    
        for place in place_results['results']:
            my_place_id = place['place_id']
            my_place_name = place['name']
            my_place_address = place['formatted_address']
            my_place_status = place['business_status']
            my_place_lat = place['geometry']['location']['lat']
            my_place_long = place['geometry']['location']['lng']
            if "International" in my_place_name:
                #print(my_place_name)
                return([my_place_lat, my_place_long])                
    else :
        print("Error in API callback result")

def hotels_call(results):
    temp = 0
    if(results['status'] == 'OK') :      
    
        for place in results['results']:
            if temp<10 :
                my_place_id = place['place_id']
                my_place_name = place['name']
                my_place_address = place['formatted_address']
                my_place_status = place['business_status']
                my_place_lat = place['geometry']['location']['lat']
                my_place_lng = place['geometry']['location']['lng']
                #my_fields = ['name', 'formatted_phone_number','type']
                #place_details = gmaps.place(place_id = my_place_id, fields = my_fields)
                #if(my_place_status=='OPERATIONAL'):
                thisdict = {
                    "name": my_place_name,
                    "address": my_place_address,
                    "co-ordinates": [my_place_lng, my_place_lat]
                }
                hotels_list.append(thisdict)
                temp += 1
                #print(my_place_name)
                #print("\t Address: " + my_place_address)
                #print("\t Place id: " + my_place_id)            
                    
    else :
        print("Error in API callback result")

    return(hotels_list)

   
# Google Places API
API_KEY = ""
gmaps = googlemaps.Client(key = API_KEY)
geolocator = geopy.geocoders.Nominatim(user_agent="MyApp")

#geo_location = geolocator.geocode("Jacksonville")
city = input("Enter destination : ")
geo_location = geolocator.geocode(city)
my_location = [geo_location.latitude,geo_location.longitude]
city_coordinates = [geo_location.longitude, geo_location.latitude]


hotels = gmaps.places(query = "hotels" ,location = my_location, radius = 30000, type = 'hotel')
hotels_list1 = hotels_call(hotels)
#pprint.pprint(hotels_list1)

if debug :
    pprint.pprint(hotels)

###################################################################################################

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', city_coordinates=city_coordinates)

@app.route('/get_hotels_call', methods=['GET'])
def get_hotels_call():
    return jsonify(hotels_list1)

if __name__ == '__main__':
    app.run(debug=True)