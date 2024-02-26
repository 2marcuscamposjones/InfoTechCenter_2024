print("\n*************************************\n")

print("Weather Branch\n")

#Import Libraries here
import random
from time import sleep

#Create a fucntion that randomly chooses the weather from a list
def Weather():
    weatherForecast = ["Snowing","Blizzard","raining","Foggy","windy","Icy","Sunny"]
    weatherConditions = random.choice(weatherForecast)
    return weatherConditions


print(Weather())