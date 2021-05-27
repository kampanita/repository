from credentials_inkubo import *
import tweepy
import random
import datetime
import time
from datetime import date


# Authenticate to Twitter
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
   
content_array = []
f=open("frases.txt","r",encoding="UTF-8") 
for line in f:
    content_array.append(line)

content_array_2 = []
f2=open("links.txt","r",encoding="UTF-8") 
for line in f2:
    content_array_2.append(line)

random.seed(time.time())
linx = content_array_2[random.randrange(len(content_array_2))]               

if datetime.date.today().weekday() == 0:
    tweettopublish = '#PutoLunes'
if datetime.date.today().weekday() == 1:
    tweettopublish = '#CabrónMartes'
if datetime.date.today().weekday() == 2:
    tweettopublish = '#DeMiércoles'
if datetime.date.today().weekday() == 3:
    tweettopublish = '#Juernes'
if datetime.date.today().weekday() == 4:
    tweettopublish = '#BenditoViernes'
if datetime.date.today().weekday() == 5:
    tweettopublish = '#SantoSabadete'
if datetime.date.today().weekday() == 6:
    tweettopublish = '#JodidoDomingo'

random.seed(time.time())
texto = ("Llevamos "+str(abs(date(2013,1,31)-date.today()).days)
        +" días sin saber quién es M.Rajoy (desde el 31-1-2013)."
        +chr(10)+content_array[random.randrange(len(content_array))]+chr(10)+linx
        +tweettopublish)

api.update_status(status=texto)

print (texto)