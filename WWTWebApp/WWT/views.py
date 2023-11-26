from django.shortcuts import render

# Welcome page and input form
def index(request):
  return render(request, 'WWT/index.html')

# Results page
def results(request):
  try:
      #Attempt to read in information from the request
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