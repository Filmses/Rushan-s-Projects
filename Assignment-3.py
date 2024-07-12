numbers = []

for i in range(5):
    x = input("Type an integer number \n")
    numbers.append(int(x))
    
print("These are the numbers you entered in:")

for i in range(len(numbers)):
    print((numbers[i]),end=" ")
    
maximum = max(numbers)
print("\nThe max number is:", maximum)

minimum = min(numbers)
print("The min number is:", minimum)

numbers.remove(maximum)
numbers.remove(minimum)

for i in range(len(numbers)):
    print((numbers[i]),end=" ")