import json
import requests


def getRegionAndMode():  # this gets the desired region and gamemode from the user
    # then puts it in a format we care about
    userregion = input("input the region ")
    userregion = "vultr-" + userregion
    usergamemode = input("enter the gamemode")
    if usergamemode == "4tdm":
        usergamemode = "4teams"
    elif usergamemode == "2tdm":
        usergamemode = "teams"
    elif usergamemode == "sbx":
        usergamemode = "sandbox"
    return userregion, usergamemode


def idToListedHex(diepid):  # this converts the server ID into a list of hex bytes (with the individual bytes reversed)
    listed = []
    for char in diepid:
        string = (hex(ord(char))[2:])
        listed.append(string[::-1])
    return listed


def toLink(diepid):  # converts the reversed bytes into a usable link
    return f"https://diep.io/#{diepid}"


def getData(usergamemode):
    url = f"https://api.n.m28.io/endpoint/diepio-{usergamemode}/findEach"
    r = requests.get(url=url)
    diepdata = r.json()
    return diepdata


def stripQuotes(stripper):
    stripped = ""
    for character in stripper:
        if character != '"':
            stripped += character
    return stripped


def getIDforRegion(reg, jsondata):
    return json.dumps(jsondata['servers'][f'{reg}']['id'])


region, gamemode = getRegionAndMode()
data = getData(gamemode)

nothex = stripQuotes(getIDforRegion(region, data))
linkEnd = idToListedHex(nothex)
linkEnd = "".join(linkEnd)
return(toLink(linkEnd))
