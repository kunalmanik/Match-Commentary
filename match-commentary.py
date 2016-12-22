#!/usr/bin/env python3
from bs4 import BeautifulSoup
import time, notify2, sys, urllib.request

#Test Statements
#url = "http://www.espn.in/football/commentary?gameId=456756" 
#url = "http://www.goal.com/en-india/match/barcelona-vs-h%C3%A9rcules/2364635/live-commentary?ICID=MP_MS_3"

url = input("Enter the link of webpage with the commentary")

#waiting time until the link refreshes and retrieves information(commentary)
wait = int(input("Enter the waiting time : "))

updates_list = list() #dummy list - Can be used to print all the commentary at once. Don't try this with notify

while True:
    page = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(page, "lxml")

    #update_card = soup('td') #espn saves content in table format
    update_card = soup('div') #goal.com saves content in divisions

    for game_detail in update_card:
            updates = game_detail.get('class', None)
            #if updates == [u'game-details']: #espn class value
            if updates == [u'text']: #goal.com class value
                update = game_detail.get_text()
                #print (update) #test-statement
                if update not in updates_list:
                    updates_list.append(update)
                    print(update + "\n")
                    notify2.init("UPDATE")
                    notify2.Notification("UPDATE", update).show()
                break
    time.sleep(wait)
