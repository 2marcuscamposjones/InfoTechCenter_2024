print("\n*************************************\n")

print("Weather Branch\n")

#Import Libraries here
import random
from time import sleep

#Create a fucntion that randomly chooses the weather from a list
def weather():
    weatherForecast = ["snowy","blizzard","rainy","foggy","windy","Icy","sunny"]
    weatherConditions = random.choice(weatherForecast)
    return weatherConditions

# Variable to call the weather() once VRS(Vehical Response System) is determined
weatherAlert = weather()

def vehicleResponseSystem():
    if weatherAlert == "snowy":
        print("\nNational Weather Service has updated our alarm by 30 minutes because of the forest of",weatherAlert,
              "weather conditions")
        print("VRS has been engaged only allowing you to drive 50mph")
    elif weatherAlert == "blizzard":
        print("\nNational Weather Service has updated our alarm by 45 minutes because of the forest of", weatherAlert,
             "weather conditions")
        print("VRS has been engaged only allowing you to drive 40mph")
    elif weatherAlert == "rainy":
        print("\nNational Weather Service has updated our alarm by 10 minutes because of the forest of", weatherAlert,
          "weather conditions")
        print("VRS has been engaged only allowing you to drive 60mph")

vehicleResponseSystem()
