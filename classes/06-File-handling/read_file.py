file=open("6-section/files/example.txt",'r')

# read()
content=file.read()
print(content)

# read() pointer back to first char
file.seek(0)

# readlines()
content=file.readlines()
print(content)

# remove '/n' from list items when storing
content=[i.rstrip("\n") for i in content]
print(content)

# close file
file.close()
