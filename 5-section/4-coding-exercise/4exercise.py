def convert_celsius(celsius):
    fahrenheit = float(celsius) * 9 / 5 + 32
    return fahrenheit

temperatures=[10,-20,-289,100]

for item in temperatures:
    if item < -273.15:
        print("-273.15 is the lowest possible number on a celsius scale")
    else:
        print("value in fahrenheit: " + str(convert_celsius(item)))

print("thank you")
