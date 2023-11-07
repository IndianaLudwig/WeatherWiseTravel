import django #Used for connecting back and front end code
import flask  #Used for geocoding maps
import json   #Used for weather reading
import pprint
import requests 

#APIs in use

#Weather: 
#Meteomatics - rain 500/day; 10 day forecast
#https://www.meteomatics.com/en/api/getting-started/
#-url with the login key
#https://universityofnorthflorida_kelly_sean:38J1BHwk5c@api.meteomatics.com
#https://api-ninjas.com/api/geocoding
#M1gxuSXmNmIfWQ7HELJD4g==KB47vGEE46Mo5LiI
#50000/month

#----------------------------------------- Visual Crossing
#Visual Crossing - 15 day forecast
#N01432610@unf.edu
#Weather
#https://www.visualcrossing.com/resources/blog/how-to-load-historical-weather-data-using-python-without-scraping/
#Key: WPFBLWYENQY3G3RMLQPX9L9DX
BaseURL = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'

ApiKey='WPFBLWYENQY3G3RMLQPX9L9DX'
#UnitGroup sets the units of the output - us or metric
UnitGroup='us'

#Location for the weather data
Location='Jacksonville,FL'
#Location = input("Location: ")

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
#pprint.pprint(x)


#enter location error catcher here



#c will display how many days you want to see
c = 0
end = 15
while (c < end):
  #this gives the date
  day = (x['days'][c]['datetime'])
  #this gives the description
  description = str(x['days'][c]['description'])
  #this givs the autocorrected address
  resolvedaddrress = str(x['resolvedAddress'])
  #this gives the temp
  temp = (x['days'][c]['temp'])
  #this is chance of rain
  precip = (x['days'][c]['precipprob'])
  #additional experimentation
  icon = str(x['days'][c]['icon'])
  precipitation = str(x['days'][c]['precip'])
  conditions = str(x['days'][c]['conditions']).lower()
  temperature = (x['days'][c]['temp'])
  precipitation = (x['days'][c]['precip'])
  windspeed = (x['days'][c]['windspeed'])
  cloudcover = (x['days'][c]['cloudcover'])
  humidity = (x['days'][c]['humidity'])
  uvindex = (x['days'][c]['uvindex'])
  snow = (x['days'][c]['snow'])

  # Initialize the weather condition
  weather_condition = "Unknown"

  #Wind Condition
  if windspeed > 50:
    weather_condition = "Extremely Windy"

  #Rainy weather
  elif "rain" in conditions or precipitation >= 1.0:
    if temperature < 50 and humidity > 70:
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
  elif cloudcover > 70 and temperature < 32:
    weather_condition = "Overcast and Cold"
  elif cloudcover > 70:
    weather_condition = "Overcast"
  elif cloudcover > 40:
    if temperature < 32:
      weather_condition = "Partialy Cloudy and Cold"
    else:
      weather_condition = "Partially Cloudy"
  elif temperature < 32 and windspeed > 20:
    weather_condition = "Cold and Windy"

  #Sunny weather
  elif temperature > 85 :
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
    
  #0 means today, 1 means tomorrow, etc
  print("\n" + "On " + str(day) + ",\n" + resolvedaddrress + ": " "\n" + description + "\n" + "Chance of rain: " + str(precip) + "%" + "\n" + "Conditions: " + conditions + "\n" + "Units: " + UnitGroup + "\n" + "Icon: " + icon)
  print("Today's Weather: " + weather_condition)
  
  c = c +1

#broken: https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Washingt,fl?&unitGroup=us&key=WPFBLWYENQY3G3RMLQPX9L9DX
#Working: https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/jacksonville,fl?&unitGroup=us&key=WPFBLWYENQY3G3RMLQPX9L9DX
#-----------------------------------------------



#Airline: 
#Aviationstack (full avaition) - price and flights with dates, begin with free
#UN: N01432610@unf.edu
#PW: Flight
#api: 397d751427b053f8b1b7fc74c58b2fda

#-----------------------------------------------
#Maps, Places: Google Maps, Leaflet
#---Please check Google Places api pricing---
#Hotels: Google Hotels
#Geocoding: Google maps, Mapquest Geocoding


#list date and weather condition
#list underneath all the dates, the condition and activies for that condition to avoid repeating 