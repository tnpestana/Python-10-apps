print ("== Improve the function by making it print out a message in case a number lower than -273.15 is passed. ==")

def convert_celsius(celsius):
    fahrenheit = float(celsius) * 9 / 5 + 32
    return fahrenheit

celsius_input = float(input("enter celsius degrees: "))

if celsius_input < -273.15:
    print("-273.15 is the lowest possible number on a celsius scale")
else:
    print("value in fahrenheit: " + str(convert_celsius(celsius_input)))

print("thank you")
