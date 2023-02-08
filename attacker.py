import requests
from time import sleep
import os

s = requests.Session()

IP = "127.0.0.1"
PORT = "5000"


class URL:
    def __init__(self, url_post, url_get):
        self.url_post = url_post
        self.url_get = url_get

url = URL(url_post=f"http://{IP}:{PORT}/command", url_get=F"http://{IP}:{PORT}/")

def sendCommand(**command):
    request = s.post(url.url_post, json=command)
    if request.status_code == 200:
        print(f"Command [ {command['command']} ] sent to the server!")
        
    else:
        print("Something Wrong!...")

def readResponse():
    request = s.get(url.url_get)
    for x in request.json():
        print(x, end="\n-----------------\n")


while True:
    readResponse()
    command = input("[ ENTER ] to Update Terminal\n\nCMD: ")
    if command == "":
        os.system("cls")
        continue
    sendCommand(command=command)
    print("\nsending command...!\n")
    sleep(4)
    os.system("cls")






