#Import Libraries Here
import time
import sys
import random
from time import sleep

#Welcome branch starts here
timeToSleep = 2

print("\n\nWelcome to InfoTech Center V1.0\n")
time.sleep(timeToSleep)

# Code to have ellipsis add a dot every 0.5 seconds
x = 0
ellipsis = 0

while x != 20:
    x += 1
    message = ("InfoTech Center Operating System Booting" +"." * ellipsis)
    ellipsis = ellipsis + 1
    sys.stdout.write("\r" + message) # \r prints a carriage return first
    time.sleep(0.5)
    if ellipsis == 4:
        ellipsis = 0
    if x == 20:
        print("\n\n Operating System Booted up - Retina Scanned - Access Granted!\n")

#Gasoline branch starts here
print("******************************************************\n")
print("Gasoline Branch\n")

# Function that list gas Levels, Randomly choosing one and returning its value
def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel
#Function that list Gas Stations, Randomly choosing one and returning its value
def listOfGasStations():
    gasStations = ["Shell","Speedway","Marathon","Circle K","Moble","Costco","Meijer","7Eleven"]
    gasStationsNearby = random.choice(gasStations)
    return gasStationsNearby
#function will call the gaslevelgauge to derermin out gas level and then find a close gastion
# if we are on Low or Quarter Tank
def gasLevelAlert():
    milesToGasStationsLow = round(random.uniform(1,25),1)
    milesToGasStationsQuarterTank = round(random.uniform(25.1,50),1)
    gasLevelIndicator = gasLevelGauge()
    if gasLevelIndicator == "Empty":
        print("***WARNING - YOU ARE ON EMPTY***")
        sleep(1.25)
        print("Calling Triple AAA")
    elif gasLevelIndicator == "Low":
        print("Your gas tank is extremely low, checking Google Maps for the closest gas stations.")
        sleep(1.25)
        print("The closest gas station is",listOfGasStations(),"which is",milesToGasStationsLow,"miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("Your gas tank is on a quarter tank, checking Google Maps for the closest gas stations.")
        sleep(1.25)
        print("The closest gas station is",listOfGasStations(),"which is",milesToGasStationsQuarterTank,"miles away.")
    elif gasLevelIndicator == "Half Tank":
        print("Your gas tank is a half of a tank full which is plenty to get to your destination.")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is at three quarter tank.")
    else:
        print("Your gas tank is full.")
gasLevelAlert()

print("\n******************************************************\n")

print("Weather Branch")

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
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 50mph")
    elif weatherAlert == "blizzard":
        print("\nNational Weather Service has updated our alarm by 45 minutes because of the forest of", weatherAlert,
             "weather conditions")
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 40mph")
    elif weatherAlert == "rainy":
        print("\nNational Weather Service has updated our alarm by 10 minutes because of the forest of", weatherAlert,
          "weather conditions")
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 60mph")
    elif weatherAlert == "foggy":
        print("\nNational Weather Service has updated our alarm by 10 minutes because of the forest of", weatherAlert,
              "weather conditions")
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 60 mph")
    elif weatherAlert == "windy":
        print("\nNational Weather Service has updated our alarm by 10 minutes because of the forest of", weatherAlert,
              "weather conditions")
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 70 mph")
    elif weatherAlert == "Icy":
        print("\nNational Weather Service has updated our alarm by 60 minutes because of the forest of", weatherAlert,
              "weather conditions")
        sleep(1.5)
        print("VRS has been engaged only allowing you to drive 30 mph")
    else:
        print("\nNational Weather Service forecasts",weatherAlert,"weather conditions")
        sleep(1.5)
        print("VRS has been disabled! Drive at your own risk")

vehicleResponseSystem()
