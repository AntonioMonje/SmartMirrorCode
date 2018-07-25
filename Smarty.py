import requests
import calendar
import time
import os
import subprocess as sp
def smartmirror():
    while True:
        print("------------------------------------")
        print("Smart Mirror starting...")
        print("CODE WRITTEN BY: ANTONIO MONJE")
        print("special thanks to Leo and Alex")
        time.sleep(5)
        tmp = sp.call('cls',shell=True)
        tmp2 = sp.call('clear',shell=True)
        print("------------------------------------")
        print("Smart Mirror starting...")
        print("CODE WRITTEN BY: ANTONIO MONJE")
        print("special thanks to Leo and Alex")
        print("Program refreshed")
        print("------------------------------------")
        #if you get user input use this code
        #city = raw_input("Enter City Name: ")
        #print(city)
        #url = api_info + city

        #get json data
        #get user input and connect to api call
        api_info = 'http://api.openweathermap.org/data/2.5/weather?appid=API-KEY-HERE&q=92069'
        json_data = requests.get(api_info).json()


        print("city_data: ")

        country_data = json_data['sys']['country']
        print("Country: " + country_data)


        city_data = json_data['name']
        print("City: " + city_data)
        city = city_data

        description_data = json_data['weather'][0]['description']
        print("Weather description: " + description_data)


        temp_data = json_data['main']['temp']
        math = temp_data
        math = math * (1.8) - 459.67
        print('Temperature in ' + city + ' is : ' + str(math))

        humidity_data = json_data['main']['humidity']
        print("Humidity is: " + str(humidity_data))

        wind_data = json_data['wind']['speed']
        print("wind speed is: " + str(wind_data))
        time.sleep(2)
        #create the calendars
        print("------------------------------------")
        print("calendar_data: ")
        if(calendar.isleap(2018)):
            print("2018 is a leap year!")
        else:
            print("2018 is not a leap year!")

        print(calendar.calendar(2018))
        print(calendar.calendar(2019))
        print(calendar.calendar(2020))
        #stop program for set amount of time
        time.sleep(600)
       


def main():  
    #call our smart mirror
    smartmirror()
    
    

if __name__ == '__main__':
    main() 