# write() method overwrites file content
file=open("6-section/files/example2.txt",'w')

lst=["Line 1\n", "Line 2\n", "Line 3\n"]

for item in lst:
    file.write(item)

file.close()
