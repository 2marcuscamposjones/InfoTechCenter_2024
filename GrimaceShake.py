print("******************************************************")
print("Gasoline Branch\n\n")

#Import Libraries Here
import random

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
    milesToGasStationsLow = random.uniform(1,25)
    milesToGasStationsQuarterTank = random.uniform(25.1,50)
    #gasLevelGauge = gasLevelGauge()
    print(milesToGasStationsLow)
    print(milesToGasStationsQuarterTank)

gasLevelAlert()
