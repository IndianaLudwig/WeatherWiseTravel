day = input('Enter the day : ')
totalDays = input('Enter the total days : ')
if (day + totalDays) > 15 :
  print('Invalid input')
else :
  conditions = str(x['days'][c]['conditions']).lower()
  temperature = (x['days'][c]['temp'])
  precipitation = (x['days'][c]['precip'])
  windspeed = (x['days'][c]['wind_speed'])
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
  