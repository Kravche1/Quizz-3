# Quizz-3

Hello! This is my Quizz-3 read file, where you can see my homework and remark!

My project is about weather. you enter name of city and the code give you your nation, city coordinates: 
latitude and longitude. also wheater is it clear or something else. after that you will see huge script look like this:

<Response [200]>    #<---- This is a server response
Status code is:  200 #<----- This is a status code is connection good or something wrong happened... 
user coordinates is:  {'lon': 44.8337, 'lat': 41.6941}
weather into tbilisi is:  [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]
City id is  800
City weather Description is  clear sky


                                                         #This is a Json File:
{           
    "coord": {
        "lon": 44.8337,
        "lat": 41.6941
    },
    "weather": [
        {
            "id": 800,
            "main": "Clear",
            "description": "clear sky",
            "icon": "01n"
        }
    ],
    "base": "stations",
    "main": {
        "temp": 287.99,
        "feels_like": 286.68,
        "temp_min": 287.99,
        "temp_max": 287.99,
        "pressure": 1016,
        "humidity": 44
    },
    "visibility": 10000,
    "wind": {
        "speed": 9.77,
        "deg": 320
    },
    "clouds": {
        "all": 0
    },
    "dt": 1652292599,
    "sys": {
        "type": 1,
        "id": 8862,
        "country": "GE",
        "sunrise": 1652233534,
        "sunset": 1652285316
    },
    "timezone": 14400,
    "id": 611717,
    "name": "Tbilisi",
    "cod": 200
}



after succesfull output nessesary information, in this example id of country, weather description and city of name will be appeared in sqlite3 database!

Thank you for attention!
