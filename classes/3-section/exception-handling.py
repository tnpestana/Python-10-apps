def divide(a,b):
    try:
        return(a/b)
    except ZeroDivisionError:
        return "zero division is not mathmatically possible"

print(divide(1,2))
print("end of program")
