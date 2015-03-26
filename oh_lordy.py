import time
from pprint import pprint



from bs4 import BeautifulSoup

import requests


## realm menu function ##
def realm_menu():
	print ""
	print ""
	print (30 * '-')
	print ("   CHOOSE YOUR REALM")
	print (30 * '-')
	print ("1. Green")
	print ("2. Red")
	print ("3. Blue")
	print (30 * '-')
 
## Get input ###
	choice = raw_input('Enter your choice [1-3] : ')
	print ""

### convert to int ###
	choice = int(choice)
 
### select realm, set url and set realm name ###
	if choice == 1:
		url = "nuklear.org/stats.html?realm=green"
        	print ("Starting Green scrape...")
		realm = url[-5:]

	elif choice == 2:
		url = "nuklear.org/stats.html?realm=red"
        	print ("Starting Red scrape...")
		realm = url[-3:]

	elif choice == 3:
        	print ("Starting Blue scrape...")
		url = "nuklear.org/stats.html?realm=blue"
		realm = url[-4:]

	else:    ## default ##
        	print ("Invalid number. Try again...")
		realm_menu()
	

realm_menu()
### sleep 1 seconds ###

time.sleep(1)
### lvl select function ###
def lvl_select():

	lvl_wanted = raw_input('What lvls do you want to display - separate by comma [1-12] : ')	
	if lvl_wanted and int(lvl_wanted) in range(1,13):
		print ""
		print ""
		print url
		print "LORD SCRAPE ",realm.upper(), "REALM"
		print ""
		print "watching for level(s) ", lvl_wanted
		print ""
	else:
		print "only levels between 1 and 12"
		lvl_select()
lvl_select()
### sleep 1 seconds ###
time.sleep(1)



r  = requests.get("http://" +url)

data = r.text

soup = BeautifulSoup(data)
for stat_row in soup.select('.statrow'):
    columns = stat_row.select('td')
    stat_rank = columns[0].text
    stat_player = columns[2].text
    stat_exp = columns[6].text 
    stat_lvl = columns[7].text
    stat_status = columns[12].text

   #rank not needed   print "Rank: " + stat_rank


    print "Player: " + stat_player
    print "Exp: " + stat_exp
    print "Lvl: " + stat_lvl
    print "Status: " + stat_status
    print ""

