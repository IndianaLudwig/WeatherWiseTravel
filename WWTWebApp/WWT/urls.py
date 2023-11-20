from django.urls import path
from . import views

app_name = "WWT"
urlpatterns = [
  # /WWT/
  path("", views.index, name="index"),
  
  # /WWT/results/
  path("results/", views.results, name="results"),
  
  # /WWT/location/locationID/
  path("location/<int:locationID>/", views.location, name="location"),
  
  # /WWT/about/
  path("about/", views.about, name="about")
]