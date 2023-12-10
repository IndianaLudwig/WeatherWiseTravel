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
car_rentals_list= []


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

def car_rentals(results):
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
                car_rentals_list.append(thisdict)
                temp += 1
                #print(my_place_name)
                #print("\t Address: " + my_place_address)
                #print("\t Place id: " + my_place_id)            
                    
    else :
        print("Error in API callback result")

    return(car_rentals_list)

   
#Google Places API
API_KEY = " "
gmaps = googlemaps.Client(key = API_KEY)
geolocator = geopy.geocoders.Nominatim(user_agent="MyApp")

#geo_location = geolocator.geocode("Jacksonville")
city = input("Enter destination : ")
geo_location = geolocator.geocode(city)
my_location = [geo_location.latitude,geo_location.longitude]
city_coordinates = [geo_location.longitude, geo_location.latitude]


if debug :
    print(geo_location)
    print(my_location)
my_place_results = gmaps.places(query = "Airport" ,location = my_location, radius = 10000, type = 'airport')
location = lat_long(my_place_results)
#print('Jacksonville:' + str(my_location))
#print('Airport: ' + str(location))
if debug :
    pprint.pprint(my_place_results)


car_rental_places = gmaps.places(query = "Car rentals near airports" ,location = location, radius = 1000, type = 'car_rental')
car_rentals_list = car_rentals(car_rental_places)

if debug :
    pprint.pprint(car_rental_places)

#pprint.pprint(car_rentals_list)

###################################################################################################

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', city_coordinates=city_coordinates)

@app.route('/get_car_rentals', methods=['GET'])
def get_car_rentals():
    return jsonify(car_rentals_list)

if __name__ == '__main__':
    app.run(debug=True)