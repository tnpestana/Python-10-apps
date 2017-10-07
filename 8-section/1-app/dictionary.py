import json

# store data.json file content on a python dictionary
data=json.load(open("8-section/1-app/data.json"))

def find_word(word):
    word=word.lower()
    if word in data:
        return data[word]
    else:
        return "sorry, couldn't find the word"

# prompt the user fo=r  a word to search
key=input("\nword to search: ")

print(find_word(key))
