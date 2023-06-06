#things that need to be tested
#- get code from twitter
#
import requests
import re, os
import time
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()


def find_between(s, first, last):
    try:
        regex = rf'{first}(.*?){last}'
        return re.findall(regex, s)
    except ValueError:
        return -1


url = 'https://www.google.com/search?q=nba+finals&rlz=1C1VDKB_enUS932US932&oq=nba+final&aqs=chrome.0.69i59j69i64j69i57j35i39i650j0i67i131i433i650j0i131i433i512j0i67i131i433i650j69i60.1431j1j7&sourceid=chrome&ie=UTF-8'
r1 = requests.get(url)
f = open("html.txt", "w")
f.write(r1.text)
f.close()
scores1 = find_between(r1.text, '<div class="BNeawe deIvCb AP7Wnd">', '</div>')
heat1, nuggets1 = int(scores1[1]), int(scores1[2])
print("current score: " +str(heat1) +"-" +str(nuggets1))
while requests.get(url).text == r1.text:
    time.sleep(.5)
print("score has updated")
r2 = requests.get(url)
scores2 = find_between(r1.text, '<div class="BNeawe deIvCb AP7Wnd">', '</div>')
heat2, nuggets2 = int(scores2[1]), int(scores2[2])
print("new score: " +str(heat2) +"-" +str(nuggets2))
if heat2-heat1==3 or nuggets2-nuggets1==3:
    twturl="https://twitter.com/ChipotleTweets"
    rtwt = requests.get(twturl)
    while find_between(rtwt.text, 'Text ', ' to 888222') == -1:
        code = find_between(rtwt.text, 'Text ', ' to 888222')
    send(code)

#from snscrape.modules.twitter import TwitterTweetScraperMode, TwitterTweetScraper
#import json, time
#import os
#
#os.system("snscrape --jsonl --max-results 10 twitter-search 'from:ChipotleTweets'> user-tweets.json")

#
#