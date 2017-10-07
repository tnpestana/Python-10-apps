print ("== Please create a function that converts Celsius degrees to Fahrenheit. ==")

def convert_celsius(celsius):
    fahrenheit = float(celsius) * 9 / 5 + 32
    return fahrenheit

celsius_input = input("enter celsius degrees: ")
print("value in fahrenheit: " + str(convert_celsius(celsius_input)))
print("thank you")
