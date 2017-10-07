import json
from difflib import get_close_matches

# store data.json file content on a python dictionary
data=json.load(open("app-1/data.json"))

# main program function for recursive calls
def main():
    # prompt the user for a word to search
    key=input("\nword to search: ")
    print(find_word(key))

# function that handles the user input
def find_word(word):
    # store input as lowercase
    word=word.lower()
    # if the word is found, iterate through the values and print them one at a time
    if word in data:
        for x in range(0, len(data[word])):
            print("> %s" % data[word][x])
        return "\nthank you"
    # if the word is not found but some similar words are, prompt the user for
    # confirmation and print the results
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
    # if no similar word is found, inform the user and quit the program
    else:
        return "sorry, couldn't find the word"

# program begins
print("\n*pestos english dictionary*")
main()
