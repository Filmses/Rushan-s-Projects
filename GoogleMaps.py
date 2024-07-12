# imports googlemaps, uses API key, and defines variables
import googlemaps
API_KEY = "AIzaSyABeEYjYxwWP37ddTsx-8-JsLGhKIEHp_Y"
maps = googlemaps.Client(key = API_KEY)
locations = []
distances = []
metrics = []
number = []
string = []
# takes input from the user for the starting location
print("Input your starting location:")
startDestination = input()
i = 0

# while loop to keep taking input from the user until they say 'STOP'
while i == 0:
    print("Input another destination (or type 'STOP' to stop adding locations):")
    endDestination = input()

    if endDestination.lower() == "stop":
        i = 1
    else:
# try and except statement to make sure nobody can enter anything too far away or to account for errors
        try:
            info = maps.directions(startDestination, endDestination)
            distance = (info[0]["legs"][0]["distance"]["text"])
            locations.append(endDestination)
            distances.append(distance)
        except IndexError:
            print("That location is too far away! Please try again!")
        except:
            print("Oops, an error occured. Please try again!")
    while i == 1:

# converts distances from a string into a number 
        for index, element in enumerate(distances):
            number.clear()
            string.clear()
            for char in element:
                if char.isdigit() or char == ".":
                    number.append(char)
                elif char.isalpha():
                    string.append(char)
                else:
                    pass
            num = "".join(number)
            metric = "".join(string)
            distances.remove(element)
            metrics.append(str(metric))
# checks whether the number should be converted into a floating point or into an integer
            if num.count(".") > 0:
                distances.insert(index, float(num))
            elif num.count(".") == 0:
                distances.insert(index, int(num))

# calculates the closest location and how long it will take to get there
        try:
            closestDistance = min(distances)
            locationNum = distances.index(closestDistance)
            closestLocation = locations[locationNum]
            info = maps.directions(startDestination, closestLocation)
            duration = (info[0]["legs"][0]["duration"]["text"])     

# prints out all the information, accounting for specific scenarios
            if len(locations) == 1:
                print("The destination you entered (" + closestLocation + ") is", min(distances), metrics[locationNum] + ".")
            else:
                print("The closest destination from", startDestination, "is", closestLocation, "which is", min(distances), metrics[locationNum] + ".")
                

            print("That distance should take around", duration, "by car.")
            i = 2
# try and except statement to make sure that the code doesn't error out if someone types 'STOP' too soon
        except:
            print("You have not entered in any other locations! Please try again!")
            i = 0