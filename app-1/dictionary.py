import json
from difflib import get_close_matches

# store data.json file content on a python dictionary
data=json.load(open("app-1/data.json"))

def main():
    # prompt the user for a word to search
    key=input("\nword to search: ")
    print(find_word(key))

def find_word(word):
    word=word.lower()
    if word in data:
        for x in range(0, len(data[word])):
            print("> %s" % data[word][x])
        return "\nthank you"
    elif len(get_close_matches(word, data.keys())) > 0:
        print("\ndid you mean %s instead?" % get_close_matches(word, data.keys())[0])
        answer=input("type Y for yes or N for no: ").lower()
        if answer=="y":
            for x in range(0, len(data[get_close_matches(word, data.keys())[0]])):
                print("> %s" % data[get_close_matches(word, data.keys())[0]][x])
            return "\nthank you"
        elif answer=="n":
            main()
        else:
            return "sorry, didn't understand the input"
    else:
        return "sorry, couldn't find the word"

# program begins
print("\n*pestos english dictionary*")
main()
