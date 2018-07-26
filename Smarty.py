import requests
import calendar
import datetime
import time
import os
import subprocess as sp

def smartmirror():
    while True:
        
        time.sleep(5)
        tmp = sp.call('cls',shell=True)
        tmp2 = sp.call('clear',shell=True)
        print('\n')
        print("------------------------------------")
        print("Smart Mirror starting...")
        print("CODE WRITTEN BY: ANTONIO MONJE")
        print("special thanks to Leo and Alex")
        print("Program refreshed")
        print datetime.datetime.utcnow()
        print("------------------------------------")
        #if you get user input use this code
        #city = raw_input("Enter City Name: ")
        #print(city)
        #url = api_info + city
        print('\n')
        #get json data
        #get user input and connect to api call
        try:
            api_info = 'http://api.openweathermap.org/data/2.5/weather?appid=API-KEY&q=92069'
            json_data = requests.get(api_info).json()
            news_api_info = ('https://newsapi.org/v2/top-headlines?'
            'country=us&'
            'apiKey=5API-KEY')
            response = requests.get(news_api_info).json()
        
            #weather for san marcos info
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
        
            #news info
            print('\n')
            print("------------------------------------")
            print("---Top 5 News Articles---")
            source_data = response['articles'][0]['source']['name']
            print("Source: " + str(source_data))
            news_title_data = response['articles'][0]['title']
            print("Article Title: " + str(news_title_data))
            news_description_data = response['articles'][0]['description']
            print("Article Description: " + str(news_description_data))
            print('\n')

            source_data1 = response['articles'][1]['source']['name']
            print("Source: " + str(source_data1))
            news_title_data1 = response['articles'][1]['title']
            print("Article Title: " + str(news_title_data1))
            news_description_data1 = response['articles'][1]['description']
            print("Article Description: " + str(news_description_data1))
            print('\n')

            source_data2 = response['articles'][2]['source']['name']
            print("Source: " + str(source_data2))
            news_title_data2 = response['articles'][2]['title']
            print("Article Title: " + str(news_title_data2))
            news_description_data2 = response['articles'][2]['description']
            print("Article Description: " + str(news_description_data2))
            print('\n')

            source_data3 = response['articles'][3]['source']['name']
            print("Source: " + str(source_data3))
            news_title_data3 = response['articles'][3]['title']
            print("Article Title: " + str(news_title_data3))
            news_description_data3 = response['articles'][3]['description']
            print("Article Description: " + str(news_description_data3))
            print('\n')

            source_data4 = response['articles'][4]['source']['name']
            print("Source: " + str(source_data4))
            news_title_data4 = response['articles'][4]['title']
            print("Article Title: " + str(news_title_data4))
            news_description_data4 = response['articles'][4]['description']
            print("Article Description: " + str(news_description_data4))
            print('\n')
        except:
            print('\n')
            print("---------------------------------------------------------------")
            print("-Error with news API or weather API. Something went wrong!    -")
            print("-weather will update next refresh                             -")
            print("-news will update next refresh                                -")
            print("---------------------------------------------------------------")
            time.sleep(5)
            smartmirror()
            break
        
        time.sleep(3)
        #create the calendars
        print("------------------------------------")
        print("calendar_data: ")
        if(calendar.isleap(2018)):
            print("2018 is a leap year!")
        else:
            print("2018 is not a leap year!")

        print(calendar.calendar(2018))
        print(calendar.calendar(2019))
        print('\n')
        print datetime.datetime.utcnow()
        print("10 mins for every refresh")
        #stop program for set amount of time
        time.sleep(600)
       


def main():  
    #call our smart mirror
    print("------------------------------------")
    print("Smart Mirror starting...")
    print("CODE WRITTEN BY: ANTONIO MONJE")
    print("special thanks to Leo and Alex")
    print datetime.datetime.utcnow()
    smartmirror()
    
    

if __name__ == '__main__':
    main() 