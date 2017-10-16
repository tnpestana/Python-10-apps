import time
from datetime import datetime as dt

# store data for future use
hots_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com", "www.instagram.com", "www.tumblr.com", "www.twitter.com"]

# while loop makes the program keep running until further notice
while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("working hours")
    else:
        print("fun hours")

    # program sleeps for 5 seconds
    time.sleep(5)
