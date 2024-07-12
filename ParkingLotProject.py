import random
import time
import sys
parkingSpotNumbers = random.sample(range(1,20),5)
parkingSpotTimes = []
i = 0

while i == 0:
    print("Welcome to X Automatic Parking Lot!")
    print("Would you like to park here? Type 'Yes' to continue")
    response = input()
    if response.lower() != "yes":
        pass
    elif response.lower() == "yes":
        i = 1
        
    while i == 1:
        print("=====================================================")
        if len(parkingSpotNumbers) != 0:
            print("Hello, we have", len(parkingSpotNumbers), "parking spots", parkingSpotNumbers, "available at this moment.")
            print("How long do you want to park? The max duration is 12 hours and the min is 0.5 hours")
            response = input()
            try:
                if float(response) > 12 or float(response) < 0.5:
                    print("An invalid selection has been made. Please try again!")
                    pass
                elif float(response) < 12 or float(response) > 0.5:
                    parkingSpotTimes.append(response)
                    i = 2
            except ValueError:
                print("An invalid selection has been made. Please try again!")
                
        if len(parkingSpotNumbers) == 0:
            print("Sorry, there are no parking spots available at this moment!")
            print("Please wait a few seconds...")
            time.sleep(5)
            print("A spot will be available in", min(parkingSpotTimes), "hours. Please come back then or reserve your spot now!")
            sys.exit(0)
            
    if i == 2:
        spot = random.choice(parkingSpotNumbers)
        print("You can park for", response, "hours at spot #" + str(spot))
        print("Thank you for using the automated parking system!")
        print("=================================================")
        parkingSpotNumbers.remove(spot)
        i = 0
    