# Get live location of user using geocoder and communicate to tempagent.py
from uagents import Agent,Context,Model
import geocoder
from uagents.setup import fund_agent_if_low

class Message(Model):
    message:str

TEMP_AGENT_ADDR = 'agent1qf4e4eedqhfuvmgkze35ujp2s68alnt29erla6fnazw9wyuwzdg7y43h7ey'

def get_location():
    cur_locate = geocoder.ip('me')
    print(cur_locate)
    # location = cur_locate.latlng
    loca = f"{cur_locate.state}, {cur_locate.country}"
    # print(loca)
    return loca

location = Agent(
    name='locationagent',
    seed='zero displacement',
    port=8001,
    endpoint=["https://127.0.0.1:8001"]
)
fund_agent_if_low(location.wallet.address())

@location.on_event("startup")
async def findlocation(ctx:Context):
    # print(get_location())
    await ctx.send(TEMP_AGENT_ADDR,Message(message=get_location()))

# location.run()
# class Location(Agent):
#     def __init__(self):
#         super().__init__()
#         self.location = None
    
#     def get_location(self):
#         curloc = geocoder.ip('me')
#         self.location = curloc.latlng
#         return self.location