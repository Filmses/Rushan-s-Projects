password = "j8925to8&Y&%^E&^$ %%&*(&421307f g0q2 b86635"
num = []
letter = []
for i in password:
    if i.isdigit():
       num.append(i)
    if i.isspace():
        pass
    else:
        letter.append(i)
print("".join(letter))
print("".join(num))
print(len(num)+len(letter))

# Function
def count_digits(string):
    count = 0
    for i in string:
        if i.isdigit():
            count += 1
        else:
            pass
    return count
print(count_digits(password))
            