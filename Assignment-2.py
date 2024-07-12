x=0

#downward triangle
for i in range(1,5):
    print("*",end="")
    for j in range(x+(i-1)):
        print("*",end="")
    print()
print("======")
    
#upward triangle
for i in range(1,5):
    print("*",end="")
    for j in range(4-i):
        print("*",end="")
    print()