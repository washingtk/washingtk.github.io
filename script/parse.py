import requests
import feedparser
from bs4 import BeautifulSoup
import re

#WSJ
# wsj_world_rss = 'https://feeds.a.dj.com/rss/RSSWorldNews.xml'
# wsj_market_rss = 'https://feeds.a.dj.com/rss/RSSMarketsMain.xml'
# wsj_tech_rss = 'https://feeds.a.dj.com/rss/RSSWSJD.xml'

#CoinDesk
coindesk_rss = 'https://www.coindesk.com/arc/outboundfeeds/rss/'
parsed = feedparser.parse(coindesk_rss)
for entry in parsed.entries:
    res = requests.get(entry.link)
    soup = BeautifulSoup(res.content, 'html.parser')
    
    title = soup.find('title').text
    p_tagged = soup.find_all('p', class_=None)
    content = ""
    for tag in p_tagged:
        content = content + tag.text
# print(title, content)


# d = feedparser.parse(wsj_market_rss)
# for entry in d.entries:
    # print(f"{entry.title}\n{entry.summary}\n{entry.link}")
# entry = d.entries[0]
# res = requests.get(entry.link)
# print(entry.link)

#read prompt and substitue article title and content
# script_dir = os.path.dirname(__file__)
# file_path = os.path.join(script_dir, 'spell.txt')
# with open(file_path, 'r') as file:
#     spell = file.read()
with open('spell.txt', 'r') as f:
    text = f.read()
pattern1 = "the article title"
pattern2 = "the content"
text = re.sub(pattern1, title, text)
text = re.sub(pattern2, content, text)

# print(text)