from django.shortcuts import render
import requests 
# Create your views here.
from .models import City
from .forms import CityForm


def index(request):
    # get the API endpoint 
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units =imperial&appid=d0aa36030de4f3b87eb0e890634879d8'
    #city = 'London'
    
    # allow user to input a new city and save it to the form
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

   # put this in context and display to the website
    form = CityForm()

# get all obejcts from City models
    cities = City.objects.all()
# get all required data from API and loop it through first and add them into a new list 
    weather_data = []

    for city in cities:
        r = requests.get(url.format(city)).json()
    #print(r.text)
        city_weather = {
        'city': city.name ,
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon':  r['weather'][0]['icon']
        
    }
        weather_data.append(city_weather)

    print(weather_data)

    #print(city_weather)
#crate a new context with the weather-data looping from the api and user input form
    context = {'weather_data': weather_data, 'form': form}

    return render(request,'weather/weatherhome.html',context)

