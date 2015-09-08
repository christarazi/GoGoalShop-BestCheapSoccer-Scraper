from pushbullet import Pushbullet
from lxml import html
import requests

def goGoalShop():
	try:
		page = requests.get('https://www.gogoalshop.com/flash-index')
		tree = html.fromstring(page.text)

		#//*[@id="gagaDealDiv"]/ul - entire list
		#//*[@id="gagaDealDiv"]/ul/li[1] - first of the list
		#//*[@id="gagaDealDiv"]/ul/li[12] - last of the list

		items = []

		for i in range(1, 13):
			xpathString = '//*[@id="gagaDealDiv"]/ul/li[' + str(i) + ']/div[2]/a/@title'
			items.append(tree.xpath(xpathString)[0])

		for elem in items:
			if "Bayern" in elem:
				print("GoGoalShop.com: Found Bayern jersey!")
				push = myPhone.push_link("GoGoalShop.com: Bayern jersey available", "https://www.gogoalshop.com/flash-index")
			#print(elem)
	except Exception as e:
		print("GoGoalShop.com: Oops! Something went wrong during scraping. Most likely items are not available yet.")
		print(e)
	else:
		print("GoGoalShop.com: Scraping ran successfully!")

def bestCheapSoccer():
	try:
		page = requests.get('http://www.bestcheapsoccer.com/flash-index')
		tree = html.fromstring(page.text)

		#//*[@id="gagaDealDiv"]/ul - entire list
		#//*[@id="gagaDealDiv"]/ul/li[1] - first of the list
		#//*[@id="gagaDealDiv"]/ul/li[12] - last of the list

		items = []

		for i in range(1, 13):
			xpathString = '//*[@id="gagaDealDiv"]/ul/li[' + str(i) + ']/div[2]/a/@title'
			items.append(tree.xpath(xpathString)[0])

		for elem in items:
			if "Bayern" in elem:
				print("BestCheapSoccer.com: Found Bayern jersey!")
				push = myPhone.push_link("BestCheapSoccer.com: Bayern jersey available", "http://www.bestcheapsoccer.com/flash-index")
			#print(elem)
	except Exception as e:
		print("BestCheapSoccer.com: Oops! Something went wrong during scraping. Most likely items are not available yet.")
		print(e)
	else:
		print("BestCheapSoccer.com: Scraping ran successfully!")

try:
	with open("api_key.txt", 'r') as fileIn:
		api_key = fileIn.read()
	pb = Pushbullet(api_key)
	myPhone = pb.devices[0]
except Exception as e:
	print(e)
else:
	goGoalShop()
	bestCheapSoccer()