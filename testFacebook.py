import feedparser
import os
import time
import sys
sys.path.append('/usr/local/lib/python2.7/dist-packages/')
import facebook

token = '601341816634019|1ds__S2_N7gIig2THoHa1mK4NiI'

graph = facebook.GraphAPI(token)
print(graph)
profile = graph.get_object('1214687540')

print(profile)

# Getting RSS feed
d = feedparser.parse('http://jsuis-un-canard.tumblr.com/rss')

title = d.entries[0].title.encode('utf8')
link = d.entries[0].link.encode('utf8')

graph.put_object('1214687540', "feed", message= title+'\n'+link)
