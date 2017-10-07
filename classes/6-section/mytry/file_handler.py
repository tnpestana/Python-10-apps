new_entry=input("new entry: ")

with open("6-section/mytry/myfile.txt", 'a') as file:
    try:
        file.write(new_entry + "\n")
        print("file updated successfully")
    except:
        print("sorry, something unexpected happened")
