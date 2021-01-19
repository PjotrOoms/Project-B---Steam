import RPi.GPIO as GPIO
import time
import json
import requests


def personastate(steamid):
    url = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=68A6A5CD1D0EE6576FCBE1486E405D46&steamids=' + steamid
    response = requests.get(url)
    data = json.loads(response.text)
    status = data['response']['players'][0]['personastate']
    if status == 1:
        return 1
    if status != 1:
        return 0


def friends(steamid):
    url = 'http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key=68A6A5CD1D0EE6576FCBE1486E405D46&steamid=' + steamid + "&relationship=friend"
    response = requests.get(url)
    data = json.loads(response.text)
    return data['friendslist']['friends']


def steamname(steamid):
    url = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=68A6A5CD1D0EE6576FCBE1486E405D46&steamids=' + steamid
    response = requests.get(url)
    data = json.loads(response.text)
    return data['response']['players'][0]['personaname']


selectedfriends = ['76561198371968392', '76561198186998210', '76561198166621811', '76561198401901151']
steamid = '76561198371968392'
ledlist = [18, 17, 4, 21]
for x in ledlist:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(x, GPIO.OUT)
while True:
    for friend in selectedfriends:
        friendname = steamname(friend)
        print(steamname(friend) + " " + str((personastate(friend))))

        if personastate(friend) == 1 and selectedfriends.index(friend) == 0:
            GPIO.output(18, GPIO.HIGH)
        elif personastate(friend) != 1 and selectedfriends.index(friend) == 0:
            GPIO.output(18, GPIO.LOW)

        elif personastate(friend) == 1 and selectedfriends.index(friend) == 1:
            GPIO.output(17, GPIO.HIGH)
        elif personastate(friend) != 1 and selectedfriends.index(friend) == 1:
            GPIO.output(17, GPIO.LOW)

        elif personastate(friend) == 1 and selectedfriends.index(friend) == 2:
            GPIO.output(4, GPIO.HIGH)
        elif personastate(friend) != 1 and selectedfriends.index(friend) == 2:
            GPIO.output(4, GPIO.LOW)

        elif personastate(friend) == 1 and selectedfriends.index(friend) == 3:
            GPIO.output(21, GPIO.HIGH)
        elif personastate(friend) != 1 and selectedfriends.index(friend) == 3:
            GPIO.output(21, GPIO.LOW)
    time.sleep(30)

