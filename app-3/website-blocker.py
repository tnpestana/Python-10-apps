import time
from datetime import datetime as dt

# store data for future use
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
hosts_temp="hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com", "facebook.com", "www.instagram.com", "www.tumblr.com"]

# while loop makes the program keep running until further notice
while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 21):
        print("working hours")
        with open(hosts_temp,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        print("fun hours")

    # program sleeps for 5 seconds
    time.sleep(5)
