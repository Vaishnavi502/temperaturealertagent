from uagents import Agent,Context,Model
import requests
import os
import geocoder
from dotenv import load_dotenv
from uagents.setup import fund_agent_if_low

load_dotenv()

user_location = None

# Get API_KEY from .env
api_key = os.getenv("API_KEY")

class Message(Model):
    message:str

def read_temp():
    # loca = "Chennai, IN"
    global user_location
    loca = user_location
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?APPID={api_key}&q={loca}&units=metric')
    curtemp = None
    if response.status_code != 200:
        raise Exception('Could not get current temperature')
    else:
        curtemp = (response.json()['main']['temp']) # Retrieve current Celcius temperature
    return curtemp

def alert_check(curtemp,min_temp,max_temp):
    if curtemp is None:
        read_temp()
    
    elif curtemp < min_temp or curtemp > max_temp:
        print('Temperature in your location is outside your preferred range!!')

# def change_range(mint,maxt):
#     if mint > maxt:
#         raise Exception("Error! Minimum temperature cannot be greater than maximum temperature!!")
#     min_temp = mint
#     max_temp = maxt

temp = Agent(
    name='tempalertagent',
    seed='nil temperature',
    port=8000,
    endpoint=["http://127.0.0.1:8000"]
    )
fund_agent_if_low(temp.wallet.address())

@temp.on_message(model=Message)
async def check(ctx:Context, sender:str, msg:Message):
    ctx.logger.info(f"Received message from {sender}:{msg.message}")
    global user_location
    user_location = msg.message

@temp.on_interval(period=1.0) # Check temperature every microsecond
async def check(ctx:Context):
    # user_location = msg.Message
    global user_location
    print(user_location)
    cur_temperature = read_temp()
    ctx.logger.info(f"Current temperature: {cur_temperature}")
    alert_check(cur_temperature,20,30)
