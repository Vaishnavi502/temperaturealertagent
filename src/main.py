from agents.temperaturealert.tempagent import temp as temperatureagent
from agents.locationpick.location import location as locationagent

if __name__ == '__main__':
    temperatureagent.run()
    locationagent.run()