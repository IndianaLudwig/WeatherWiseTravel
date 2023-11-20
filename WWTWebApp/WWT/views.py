from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Welcome page and input form
def index(request):
  return render(request, 'WWT/index.html')

# Results page
def results(request):
  try:
      #Attempt to read in information from the request
      origin = request.POST["origin"]
      destination = request.POST["destination"]
      arrival = request.POST["arrival"]
      departure = request.POST["departure"]
  except (KeyError):
      #Information was missing from the request, redirect to index page
      return render(request, 'WWT/index.html')
  else:
      #Information from the request was collected, direct to results page
      context = {"origin": origin, "destination": destination, "arrival": arrival, "departure": departure}
      return HttpResponseRedirect(reverse("WWT:results2", kwargs=context)) #need to re-add the ability to have a url with the parameters
      return render(request, 'WWT/results.html', context)
  
def results2(request, origin, destination, arrival, departure):
   context = {"origin": origin, "destination": destination, "arrival": arrival, "departure": departure}
   return render(request, 'WWT/results.html', context)

# Location details page
def location(request, locationID):
  context = {"locationID": locationID}
  return render(request, 'WWT/location.html', context)

# About page
def about(request):
  return render(request, 'WWT/about.html')