import requests
import datetime

def weather():
    data = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Kyiv&appid=e6125469fdc9299b59d07b130ac1b38e')
    description = data.json()['weather'][0]['description']
    celcius = round(data.json()['main']['temp'] - 273.15, 1)
    return 'Today is {}\n\n\n{}\nTemp {}°C'.format(datetime.date.today().strftime("%A %d"), description.upper(), celcius)

