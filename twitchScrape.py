from selenium import webdriver
from datetime import datetime

import webbrowser
import time
import json

browser = webdriver.Firefox()

url = 'http://twitch.tv/directory/game/'
browser.get(url)
time.sleep(2)
streamerLinks = []
gameLinks = []
count = 0
cName = []
cViewers = []
sName = []
sViewers = []
sViewersNUM = []
cViewersNUM = []
now = datetime.now()
dt_string = now.strftime("%m/%d/%Y %H:%M:%S")



catagoryViews = browser.find_elements_by_xpath("//p[@class='tw-c-text-alt-2 tw-ellipsis']")
catagoryName = browser.find_elements_by_xpath("//div[@class='tw-ellipsis tw-flex-grow-1 tw-flex-shrink-1 tw-mg-t-05']")


for i in catagoryName:
    cName.append(i.text)
for i in catagoryViews:
    cViewers.append(i.text)
for a in catagoryName:
    if(count < 5):
        gameLinks.append((url)+a.text)
        print(a.text)
        count+=1
count = 0
print(*gameLinks)

for i in catagoryViews:
    print(i.text)

print(*streamerLinks)

for i in range(5):
    newLink = gameLinks[i]
    print(newLink)
    finalLink = newLink+"?sort=VIEWER_COUNT"
    print(finalLink)
    browser.get(finalLink)
    time.sleep(2)
    streamerNames = browser.find_elements_by_xpath("//p[@class='tw-c-text-alt-2 tw-ellipsis']")
    for j in streamerNames:
        sName.append(j.text)
        print(j.text)
    streamerViewers = browser.find_elements_by_xpath("//div[@class='tw-absolute tw-bottom-0 tw-left-0 tw-mg-1']")
    for k in streamerViewers:
        sViewers.append(k.text)
        print(k.text)


finalList1 = []
finalList2 = []
for str in cViewers:
    newC = str.replace('k', '')
    cViewersNUM.append(newC)
    count+=1
count = 0
for str in sViewers:
    newS = str.replace('k', '')
    sViewersNUM.append(newS)
    count+=1
count = 0
finalList1.append(dt_string)
for i in range(len(cName)):
    finalList1.append(cName[i])
    finalList1.append(":  ")
    finalList1.append(cViewersNUM[i])
    finalList1.append("\n")

print(*finalList1)
print("---------------------------------")

for i in range(len(sName)):
    finalList2.append(sName[i])
    finalList2.append(":  ")
    finalList2.append(sViewersNUM[i])
    finalList2.append("\n")

print(*finalList2)
print("--------------------------------")

print(*sName)
print(*sViewersNUM)

with open("data.json","a") as f:
    json.dump(finalList1, f)
    json.dump(finalList2, f)
browser.close()
