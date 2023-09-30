from agents.temperaturealert.tempagent import TemperatureAlert as temperatureagent
from agents.temperaturealert.tempagent import Location as locationagent

if __name__ == '__main__':
    locationagent = Location()
    locationagent.run()

    temperatureagent = TemperatureAlert(locationagent,10,20)
    temperatureagent.run()