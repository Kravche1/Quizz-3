import requests
import json
import sqlite3
# მომხმარებელს შემოაქ ქალაქის დასახელება. რომელიც უნდა ჩაისეტოს API ლინკში
user_city = input("Please enter name of city: ")

# ე.წ. API KEy
key = '054673ab62682da2ab8c7abd6c098ecf'

request_to_api = f'https://api.openweathermap.org/data/2.5/weather?q={user_city}&appid={key}'

# status code request
request_to_server = requests.get(request_to_api)
print(request_to_server)
print("Status code is: ", request_to_server.status_code)


# json file-ის გადაყვანა Dictionary-ში რათა მივწვდეთ Key-ებს.

request_to_server_dict = json.loads(request_to_server.text)

print("user coordinates is: ", request_to_server_dict['coord'])
print("weather into tbilisi is: ", request_to_server_dict['weather'])


id = request_to_server_dict['weather'][0]['id']
description = request_to_server_dict['weather'][0]['description']
print("City id is ",id)
print("City weather Description is ", description)



# beauty of json file
print(json.dumps(request_to_server_dict, indent=4))

#SQLITE3
connect = sqlite3.connect("Weather.db")
cursor = connect.cursor()

new_sql_base = '''CREATE TABLE IF NOT EXISTS WEATHER_INTO_CITIES(
   CITY_NAME VARCHAR(20) NOT NULL,
   id INT,
   description VARCHAR(40)
)'''

insert = f'INSERT INTO WEATHER_INTO_CITIES (CITY_NAME, id, description) values ({user_city}, {id}, {description})'


cursor.execute(insert)
connect.commit()
connect.close()




