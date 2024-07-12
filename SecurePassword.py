i = 1
while i == 1:
    chars = []
    specialchars = set()
    digits = 0
    uppercase = 0
    lowercase = 0
    print("Type the password you want to use. It must have:")
    print("- 8 characters")
    print("- Only one of these special characters: ($,#,*,%,@)")
    print("- Uppercase and lowercase letters")
    print("- At least 2 digits")
    print("===================================================")
    password = input()
    for char in password:
        chars.append(char)
        if char.isdigit():
            digits += 1
        if char.isupper():
            uppercase += 1
        if char.islower():
            lowercase += 1
        if char == "$" or char == "#" or char == "*" or char == "%" or char == "@":
            specialchars.add(char)
    if len(chars) >= 8 and len(specialchars) == 1 and uppercase >= 1 and lowercase >= 1 and digits >= 2:
        print("=================================")
        print("You have chosen a valid password!")
        i = 2
    else:
        print("================================================================")
        print("Your password does not match the requirements. Please try again.")
        print("================================================================")
    while i == 2:
        print("=================================")
        print("Please confirm your password.")
        print("=================================")
        confirmation = input()
        if confirmation == password:
            print("You have successfully created your password!")
            i = 3
        elif confirmation != password:
            print("Sorry, those passwords do not match. Please try again.")
        
        
        
        
    
