import datetime

# store current date and time 
filename=datetime.datetime.now()

def create_file():
    # strftime() method provides a string format for the datetime object
    with open("7-section/time_files/"+filename.strftime("%Y-%m-%d--%H-%M")+".txt", "w") as file:
        file.write("")

create_file()
