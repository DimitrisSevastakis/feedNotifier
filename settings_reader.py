import json, ast

class settings_reader(object):

	def __init__(self):
		settings = ''
		with open("settings.json") as f:
			settings = ast.literal_eval(json.dumps(json.loads(f.read())))
		self.user = {}
		self.user['name'] = settings['email']['user']
		self.user['pass'] = settings['email']['pass']
		self.feeds = settings['feeds']


	def get_user(self):
		return self.user

	def get_feeds(self):
		return self.feeds