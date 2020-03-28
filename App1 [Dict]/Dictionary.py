import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def return_meaning(word):
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        match = get_close_matches(word, data.keys())[0]
        get_ans = input("Did You mean {}. Enter Y if yes, anyother key if No: " .format(match))
        if get_ans == 'Y':
            return data[match]
        else: 
            return "Word doesn't exist" 
    else:
        return "Word doesn't exist"

word = input("Enter Word: ")

Ans = return_meaning(word.lower())
if type(Ans) == list:
    for i in Ans:
        print ("{}: {}" .format(word, i))
else:
    print ("{}: {}".format(word, Ans))
