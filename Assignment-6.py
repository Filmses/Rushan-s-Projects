# Function #1 (finding the second largest number)
def second_max(list):
    list.remove(max(list))
    return max(list)

numbers = [1,2,3,4,5]
print(second_max(numbers))

# Function #2 (finding how many letters are in a string)
def letter_count(txt, letter):
    txt = txt.lower()
    return txt.count(letter)

string = "Python is cool"
print(letter_count(string, "y"))

# Function #3 (finding the longest and shortest word in a string)
def longest_word(txt):
    word = []
    word2 = []
    txt = txt.split()
    for i in txt:
        word.clear()
        for j in i:
            word.append(j)
        if len(word) > len(word2):
            word2 = word.copy()
        else:
            pass
    
    return "".join(word2)

def shortest_word(txt):
    word = []
    word2 = []
    for i in range(0,1000):
        word2.append("e")
    txt = txt.split()
    for i in txt:
        word.clear()
        for j in i:
            word.append(j)
        if len(word) <= len(word2):
            word2 = word.copy()
        else:
            pass
    
    return "".join(word2)
            

print(longest_word(string))
print(shortest_word(string))
        


    