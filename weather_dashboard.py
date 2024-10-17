import requests

api_key = 'e60cff43deac06c20ed14335acc25c76'

base_url = 'http://api.openweathermap.org/data/2.5/weather?'

city_name = input('Enter city name: ')

complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"

response = requests.get(complete_url)

data = response.json()

if data['cod'] != '404':
    main = data['main']
    weather = data['weather'][0]

    temperature = main['temp']
    humidity = main['humidity']
    description = weather['description']

    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Weather Description: {description.capitalize()}")
else:
    print('City Not Found!')
