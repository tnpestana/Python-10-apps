import datetime

filename=datetime.datetime.now()

def create_file():
    with open("7-section/time_files/"+filename.strftime("%Y-%m-%d--%H-%M")+".txt", "w") as file:
        file.write("")

create_file()
