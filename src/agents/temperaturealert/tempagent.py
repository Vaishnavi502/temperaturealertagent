from uagents import Agent
import requests
import os
import geocoder
from dotenv import load_dotenv

load_dotenv()

# Get API_KEY from .env
api_key = os.getenv("API_KEY")
class TemperatureAlert(Agent):
    def __init__(self, location, min_temp, max_temp):
        super().__init__()
        self.location = location
        self.min_temp = min_temp
        self.max_temp = max_temp

        self.curtemp = None
    
    def read_temp(self):
        loca = self.location.get_location()
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?APPID={api_key}&q={loca}')
        if response.status_code != 200:
            raise Exception('Could not get current temperature')
        else:
            self.curtemp = response.json()['main']['temp'] # Retrieve current Celcius temperature
            print("Current temperature:",self.curtemp)
    
    def alert_check(self):
        if self.curtemp is None:
            self.read_temp()
        
        elif self.curtemp < self.min_temp or self.curtemp > self.max_temp:
            print('Temperature in your location is outside your preferred range!!')
    
    def change_range(self,min_temp,max_temp):
        if min_temp > max_temp:
            raise Exception("Error! Minimum temperature cannot be greater than maximum temperature!!")
        self.min_temp = min_temp
        self.max_temp = max_temp

class Location(Agent):
    def __init__(self):
        super().__init__()
        self.location = None
    
    def get_location(self):
        curloc = geocoder.ip('me')
        self.location = curloc.latlng
        return self.location



# temp = Agent(
#     name='detecttemp',
#     seed='nil temperature',
#     )

# location = Agent(
#     name='location',
#     seed='none'
# )