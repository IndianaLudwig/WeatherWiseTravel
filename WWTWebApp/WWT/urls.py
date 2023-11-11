from django.urls import path
from . import views

app_name = "WWT"
urlpatterns = [
  # /WWT/
  path("", views.index, name="index"),
  
  # /WWT/results/origin/destination/arrival/departure/
  path("results/<str:origin>/<str:destination>/<str:arrival>/<str:departure>/", views.results, name="results"),
  
  # /WWT/location/locationID/
  path("location/<int:locationID>/", views.location, name="location"),
  
  # /WWT/about/
  path("about/", views.about, name="about")
]