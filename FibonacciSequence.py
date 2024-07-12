firstTerm = 0
secondTerm = 1
count = 0
fibonacci = []
print("Type the number of terms you want to see:")
nextTerm = input()
fibonacci.append(firstTerm)
fibonacci.append(secondTerm)
print(firstTerm)
print(secondTerm)
for i in range(0, int(nextTerm)-2):
    fibonacci.append(fibonacci[count] + fibonacci[count+1])
    print(fibonacci[count+2])
    count += 1