# THIS SCRIPT HAS AN ASSOCIATED TASK (Website Blocker) IN TASK SCHEDULER
# IF THE TASK IS ACTIVATED IT WILL RUN AT STARTUP AND STAY IN BACKGROUND

import time
from datetime import datetime as dt

# store data for future use
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
hosts_temp="hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com", "facebook.com", "www.instagram.com", "www.tumblr.com"]

# while loop makes the program keep running until further notice
while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("working hours")
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        print("fun hours")
        with open(hosts_path,'r+') as file:
            # readlines() devolve uma lista com todas as linhas do ficheiro
            content=file.readlines()
            # the readlines() method moves the pointer to the last character
            # move file pointer to the first character again
            file.seek(0)
            # iterate through all stored lines
            for line in content:
                # check if any website of the list is in this line
                if not any(website in line for website in website_list):
                    # if not, the line is safe to write
                    file.write(line)
                file.truncate()

    # program sleeps for 5 seconds
    time.sleep(5)
