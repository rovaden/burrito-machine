import datetime
import time
done = False
start = datetime.datetime.now()
from playsound import playsound
import requests
import re
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()
import pyautogui as pyg
import snscrape.modules.twitter as sntwitter
import pandas as pd
from IPython.display import display

def get_latest_tweet():
    # Creating list to append tweet data to
    tweets_list1 = []

    # Using TwitterSearchScraper to scrape data and append tweets to list
    for tweet in enumerate(sntwitter.TwitterSearchScraper('from:ChipotleTweets').get_items()):
        if tweet.rawContent.startswith('@')==False:
            return tweet.rawContent
    return None

def find_coord():
    try:
        while True:
            x, y = pyg.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print('\n')

def send_gv(code):
    pyg.hotkey('alt', 'tab')
    pyg.click(x=403, y=17)
    pyg.click(x=459, y=1011)
    pyg.write(code)
    pyg.click(x=933, y=1011)
    pyg.hotkey('alt', 'tab')

def find_between(s, first, last):
    try:
        regex = rf'{first}(.*?){last}'
        return re.findall(regex, s)
    except ValueError:
        return -1

def get_scores():
    url = 'https://www.google.com/search?q=nba+finals&rlz=1C1VDKB_enUS932US932&oq=nba+final&aqs=chrome.0.69i59j69i64j69i57j35i39i650j0i67i131i433i650j0i131i433i512j0i67i131i433i650j69i60.1431j1j7&sourceid=chrome&ie=UTF-8'
    r1 = requests.get(url)
    f = open("scores.txt", "w")
    f.write(r1.text)
    f.close()
    scores = find_between(r1.text, '<div class="BNeawe deIvCb AP7Wnd">', '</div>')
    print("heat: "+ str(scores[1] +"; nuggests: " + str(scores[2])))
    return [scores[1], scores[2]]

def check_threes(prev):
    new = get_scores()
    if prev[0]-new[0]==3 or prev[1]-new[1]==3:
        return True
    else:
        return False
    
def score_notif():
    og = get_scores()
    while og == get_scores():
        print("no change")
        time.sleep(1)
    return og

def get_code():
    og =find_between(get_latest_tweet(), "Text ", " to 888222")[0]
    new = find_between(get_latest_tweet(), "Text ", " to 888222")[0]
    while og == new:
        print("waiting for new code")
        new = find_between(get_latest_tweet(), "Text ", " to 888222")[0]
    return new

print(get_scores())
#while not done:
#    org= score_notif()
#    if check_threes(org):
#        send_gv(get_code())
#        playsound('/yippe.mp3')
#    if datetime.datetime.now() - start >= datetime.timedelta(hours=4):
#        done = True
#playsound('yippee.mp3')