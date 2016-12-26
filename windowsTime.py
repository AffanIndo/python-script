
"""
windowsTime.py
My computer's CMOS is busted so the time oftenly resetted. This program set it automatically by using UTC internet time. This program using "date" program on windows, "elevate" program on windows http://code.kliu.org/misc/elevate/, bs4 and requests module.
bashrc: alias windowsTime="cd /d/PROGRAMMING/git/python-script/ && source /d/PROGRAMMING/git/python-script/my_env/Scripts/activate && python windowsTime.py"
"""

from bs4 import BeautifulSoup
import requests
from os import system

timezone = 7

r = requests.get("http://just-the-time.appspot.com/")

data = r.text
hour = (int(data[11:13:]) + timezone) % 24
data = data[:11] + str(hour) + data[13:]

date = data.split(" ")[0]
time = data.split(" ")[1]

date = date.replace("-", "/")

day = date.split("/")[0]
month = date.split("/")[1]
year = date.split("/")[2]

date = year + "/" + month + "/"  + day

print("\n\nNow the program will launch elevated CMD. Enter these command:")
print("date " + date + " && " +"time " + time + "\n\n")
system("elevate cmd")