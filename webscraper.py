import requests
from bs4 import BeautifulSoup
import pandas as pd

page =  requests.get('https://forecast.weather.gov/MapClick.php?lat=34.05349000000007&lon=-118.24531999999999#.Xf8YmkczbIU')

soup = BeautifulSoup(page.content,'html.parser')
week = soup.find(id='seven-day-forecast-body')
items = week.find_all(class_='tombstone-container')
#print(items[0])

'''print(items[i].find(class_='period-name').get_text())
print(items[i].find(class_='short-desc').get_text())
print(items[i].find(class_='temp').get_text())'''

period_names = [item.find(class_='period-name').get_text() for item in items]
#print(period_names)
description = [item.find(class_='short-desc').get_text() for item in items]
#print(description)
temperature = [item.find(class_='temp').get_text() for item in items]
#print(temperature)


dictionary = {
    'Period': period_names,
    'Description': description,
    'Temperature': temperature
    }

weather_stuff = pd.DataFrame(dictionary)

print(weather_stuff)

weather_stuff.to_csv('weather.csv')