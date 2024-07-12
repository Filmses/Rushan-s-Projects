def is_palindrome(word):
    word = word.lower()
    list = []
    for i in word:
        if i == " ":
            pass
        else:
            list.append(i)
    list2 = list.copy()
    list2.reverse()
    if list2 == list:
        return True
    else:
        return False


def removeDuplicates(list):
   index = 0
   for i in list:
       if list.count(i) > 1:
           list.pop(index)
       index += 1
    
duplicates = [1, 2, 2, 2, 3, 4, 3, 2, 6, 5]
removeDuplicates(duplicates)
print(duplicates)  