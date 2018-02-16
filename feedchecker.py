import feedparser
import sys
import unicodedata
import pickle
import email_notifier
from email.mime.text import MIMEText
from settings_reader import settings_reader
import time


try:
	parsed_items = pickle.load( open( "save.p", "rb" ) )
except:
	parsed_items = {}


settings = settings_reader()
mail = email_notifier.mailNotifier(settings.get_user()['name'], settings.get_user()['pass'])
feeds = settings.get_feeds()

while True:
	# loop over all links
	for feed_link in feeds.keys():
		feed = feedparser.parse(feed_link)
		for item in feed['items']:
			#in every feed check all published items
			
			#hash the item and check if it has already been processed
			if not parsed_items.has_key(hash(item['date'] + item['title'] + item['link'])):
				parsed_items[hash(item['date'] + item['title'] + item['link'])] = 1
				title = unicodedata.normalize('NFKD', item['title']).encode('ascii','ignore')
				title_l = title.lower()
				pickle.dump( parsed_items, open( "save.p", "wb" ) )
				print(feeds[feed_link]['keys'])
				
				#check each item for specified keys
				for key in feeds[feed_link]['keys']:
					
					if key.lower() in title_l:
						#key is found, send email
						print('%s found in %s. Notifying..' %(key, feed_link))
						#notify user
						subject = 'New release: %s' %title
						body = '%s is out! Read here:\n %s' %(title, item['link'])
						mail.send_email(subject, body, settings.get_user()['name'])
	time.sleep(10)

		

