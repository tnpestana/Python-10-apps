import datetime
import glob2

# store current date and time
filename=datetime.datetime.now()
# sample files as a list
filelist=glob2.glob("7-section/6-coding-exercise/sample-files/*")

def create_file():
    # strftime() method provides a string format for the datetime object
    with open("7-section/6-coding-exercise/my-file/"+filename.strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt", "w") as file:
        for item in filelist:
            with open(item, "r") as file2:
                content=file2.read()
                file.write(content+"\n")

create_file()
