#! /usr/bin/python3

import bs4, requests
from selenium import webdriver

def getBentonvilleWeather(weatherUrl):
    res = requests.get(weatherUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elemsOne = soup.select('#current_conditions-summary > p.myforecast-current')
    
    return elemsOne[0].text.strip()
   
def getBentonvilleTemp(tempUrl):
    res = requests.get(tempUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elemsTwo = soup.select('#current_conditions-summary > p.myforecast-current-lrg')

    return elemsTwo[0].text.strip()



weather = getBentonvilleWeather('https://forecast.weather.gov/MapClick.php?lat=36.368930000000034&lon=-94.21025999999995')
temp = getBentonvilleTemp('https://forecast.weather.gov/MapClick.php?lat=36.368930000000034&lon=-94.21025999999995')

browser = webdriver.Chrome()
browser.get('https://forecast.weather.gov/MapClick.php?lat=36.368930000000034&lon=-94.21025999999995')
elem = browser.find_element_by_css_selector('#localWFO')
elem.click()


print('The current weather in Bentonville is ' + weather + ' and ' + temp)

