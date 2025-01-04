from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    weather_data = None  # Initialize weather data
    error_message = None  # Initialize error message

    if request.method == 'POST':
        city = request.POST.get('city')
        if city:
            weather_data = get_weather_data(city)
            if 'error' in weather_data:  # Check if an error key exists
                error_message = "Please enter the correct city name."
        

    return render(request, 'home.html', {'weather_data': weather_data, 'error_message': error_message})


def get_weather_data(city):
    api_key = 'Your-API -KEY' # enter your API key 
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()

    if data.get('cod') == 200:  # Ensure a valid city is found
        return {
            'city': city,
            'temperature': data['main']['temp'],
            'weather': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
        }
    else:
        return {'error': 'City not found'}  # Return an error key for invalid cities
