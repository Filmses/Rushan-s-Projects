a = "123-450-5679"
aSplit = a.split("-")

for i in range(len(aSplit)):
    print(aSplit[i])

string = []
b = "How do you split a string??"
bSplit = b.split()
for i in range(len(bSplit)-2):
    string.append(bSplit[i])
print(" ".join(string))

accountInfo = "Name-Sam,Age-22,Account-23456"
accountSplit = accountInfo.split(",")
accountSplit = "-".join(accountSplit)
accountSplit = accountSplit.split("-")
for i in range(len(accountSplit)):
    if i % 2 != 0:
        print(accountSplit[i])
    else:
        pass
    
    
