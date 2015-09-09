from pushbullet import Pushbullet
from lxml import html
import requests
import time

def goGoalShop():
	try:
		page = requests.get('https://www.gogoalshop.com/flash-index')
		tree = html.fromstring(page.text)

		#//*[@id="gagaDealDiv"]/ul - entire list
		#//*[@id="gagaDealDiv"]/ul/li[1] - first of the list
		#//*[@id="gagaDealDiv"]/ul/li[12] - last of the list

		items = []

		for i in range(1, 13):
			xpathString = '//*[@id="gagaDealDiv"]/ul/li[' + str(i) + ']/div[2]/a/text()'
			items.append(tree.xpath(xpathString)[0])

		for elem in items:
			if "Bayern" in elem:
				print(time.strftime("%a %m/%d/%y %I:%M:%S") + " | GoGoalShop.com: Found Bayern jersey!")
				push = myPhone.push_link("GoGoalShop.com: " + elem, "https://www.gogoalshop.com/flash-index")
			if "Arsenal" in elem:
				print(time.strftime("%a %m/%d/%y %I:%M:%S") + " | GoGoalShop.com: Found Barcelona jersey!")
				push = myPhone.push_link("GoGoalShop.com: " + elem, "https://www.gogoalshop.com/flash-index")
			if "Barcelona" in elem:
				print(time.strftime("%a %m/%d/%y %I:%M:%S") + " | GoGoalShop.com: Found Barcelona jersey!")
				push = myPhone.push_link("GoGoalShop.com: " + elem, "https://www.gogoalshop.com/flash-index")

	except Exception as e:
		print(time.strftime("%a %m/%d/%y %I:%M:%S") + " | GoGoalShop.com: Oops! Something went wrong during scraping. Most likely items are not available yet.")
		print(time.strftime("%a %m/%d/%y %I:%M:%S") + " | " + e)
	else:
		print(time.strftime("%a %m/%d/%y %I:%M:%S") + " | GoGoalShop.com: Scraping ran successfully!")

def bestCheapSoccer():
	try:
		page = requests.get('http://www.bestcheapsoccer.com/flash-index')
		tree = html.fromstring(page.text)

		items = []

		for i in range(1, 13):
			xpathString = '//*[@id="gagaDealDiv"]/ul/li[' + str(i) + ']/div[2]/a/@title'
			items.append(tree.xpath(xpathString)[0])

		for elem in items:
			if "Bayern" in elem:
				print(time.strftime("%a %m/%d/%y %I:%M:%S") + " | BestCheapSoccer.com: Found Bayern jersey!")
				push = myPhone.push_link("BestCheapSoccer.com: " + elem, "http://www.bestcheapsoccer.com/flash-index")
			if "Arsenal" in elem:
				print(time.strftime("%a %m/%d/%y %I:%M:%S") + " | BestCheapSoccer.com: Found Barcelona jersey!")
				push = myPhone.push_link("BestCheapSoccer.com: " + elem, "http://www.bestcheapsoccer.com/flash-index")
			if "Barcelona" in elem:
				print(time.strftime("%a %m/%d/%y %I:%M:%S") + " | BestCheapSoccer.com: Found Barcelona jersey!")
				push = myPhone.push_link("BestCheapSoccer.com: " + elem, "http://www.bestcheapsoccer.com/flash-index")

	except Exception as e:
		print(time.strftime("%a %m/%d/%y %I:%M:%S") + " | BestCheapSoccer.com: Oops! Something went wrong during scraping. Most likely items are not available yet.")
		print(time.strftime("%a %m/%d/%y %I:%M:%S") + " | " + e)
	else:
		print(time.strftime("%a %m/%d/%y %I:%M:%S") + " | BestCheapSoccer.com: Scraping ran successfully!")

try:
	with open("api_key.txt", 'r') as fileIn:
		api_key = fileIn.read().strip()
		pb = Pushbullet(api_key)
		myPhone = pb.devices[0]
except Exception as e:
	print(time.strftime("%a %m/%d/%y %I:%M:%S") + " | Something went wrong with the Pushbullet.")
else:
	goGoalShop()
	bestCheapSoccer()
