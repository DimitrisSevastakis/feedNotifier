import json, ast

class settings_reader(object):

	def __init__(self):
		self.settings = ''
		with open("settings.json") as f:
			self.settings = ast.literal_eval(json.dumps(json.loads(f.read())))
		self.user = {}
		self.user['name'] = self.settings['email']['user']
		self.user['pass'] = self.settings['email']['pass']
		self.feeds = self.settings['feeds']


	def get_user(self):
		return self.user

	def get_feeds(self):
		return self.feeds

	def get_settings(self):
		return self.settings['settings']