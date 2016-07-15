from lxml import html
import requests

page = requests.get('https://www.reddit.com/r/GlobalOffensiveTrade/new/.json')
tree = html.fromstring(page.content)

deals = tree.xpath('@href')

print deals
