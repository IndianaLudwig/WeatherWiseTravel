from django.shortcuts import render

# Welcome page and input form
def index(request):
  return render(request, 'WWT/index.html')

# Results page
def results(request):
  
  context = {"origin": origin, "destination": destination, "arrival": arrival, "departure": departure}
  return render(request, 'WWT/results.html', context)

# Location details page
def location(request, locationID):
  context = {"locationID": locationID}
  return render(request, 'WWT/location.html', context)

# About page
def about(request):
  return render(request, 'WWT/about.html')