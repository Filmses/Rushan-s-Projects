maxParkTime = 0.5
for i in range(0,5):
    print("For how long do you want to park your car?")
    parkTime = input()
    if float(parkTime) > float(maxParkTime):
        maxParkTime = parkTime
    else:
        pass
    
print("The max number is:", maxParkTime)

minParkTime = 10
for i in range(0,5):
    print("For how long do you want to park your car?")
    parkTime = input()
    if float(parkTime) < float(minParkTime):
        minParkTime = parkTime
    else:
        pass
    
print("The min number is:", minParkTime)