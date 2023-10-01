# Get live location of user using geocoder and communicate to tempagent.py
from uagents import Agent,Context,Model
import geocoder
from uagents.setup import fund_agent_if_low

class Message(Model):
    message:str

TEMP_AGENT_ADDR = 'agent1qf4e4eedqhfuvmgkze35ujp2s68alnt29erla6fnazw9wyuwzdg7y43h7ey'

location = Agent(
    name='locationagent',
    seed='zero displacement',
    port=8001,
    endpoint=["https://127.0.0.1:8001"]
)

def get_location():
    cur_locate = geocoder.ip('me')
    # location = cur_locate.latlng
    location = f"{cur_locate.city}, {cur_locate.country}"
    print(location)
    return location

fund_agent_if_low(location.wallet.address())


# class Location(Agent):
#     def __init__(self):
#         super().__init__()
#         self.location = None
    
#     def get_location(self):
#         curloc = geocoder.ip('me')
#         self.location = curloc.latlng
#         return self.location