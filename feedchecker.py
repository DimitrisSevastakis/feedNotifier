import feedparser
import sys
import unicodedata
import pickle
import email_notifier
from email.mime.text import MIMEText
import time

argv = sys.argv

#url to scan
url = argv[1]
#entry to look for
target = argv[2].lower()
#email for notification
target_email = user ='dsevastakis@gmail.com'
pwd = 'Y!JMW3#@!'

try:
	parsed_items = pickle.load( open( "save.p", "rb" ) )
except:
	parsed_items = {}


mail = email_notifier.mailNotifier(user, pwd)

while True:
	feed = feedparser.parse(url)
	for item in feed['items']:
		if not parsed_items.has_key(hash(item['date'] + item['title'] + item['link'])):
			parsed_items[hash(item['date'] + item['title'] + item['link'])] = 1
			title = unicodedata.normalize('NFKD', item['title']).encode('ascii','ignore')
			title_l = title.lower()
			pickle.dump( parsed_items, open( "save.p", "wb" ) )
			if target in title_l:
				print('target found')

				#notify user
				subject = 'New release: %s' %title
				body = '%s is out! Read here:\n %s' %(title, item['link'])
				mail.send_email(subject, body, target_email)
				exit()
	time.sleep(10)

		

