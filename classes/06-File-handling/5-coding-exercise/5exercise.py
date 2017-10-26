def convert_celsius(celsius):
    fahrenheit = float(celsius) * 9 / 5 + 32
    return fahrenheit

temperatures=[10,-20,-289,100]

# open file
with open("6-section/5-coding-exercise/text_file.txt", 'w') as file:

    for item in temperatures:
        if item >= -273.15:
            file.write("value in fahrenheit: " + str(convert_celsius(item)) + "\n")
