import os
import smtplib


class mailNotifier(object):
	def __init__(self, user, pwd):
		self.user = user
		self.pwd = pwd

	def send_email(self, subject, body, recipient):
		FROM = self.user
		TO = recipient if type(recipient) is list else [recipient]
		SUBJECT = subject
		TEXT = body

		# Prepare actual message
		message = """From: %s\nTo: %s\nSubject: %s\n\n%s
		""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
		try:
			server = smtplib.SMTP("smtp.gmail.com", 587)
			server.ehlo()
			server.starttls()
			server.login(self.user, self.pwd)
			server.sendmail(FROM, TO, message)
			server.close()
			print 'successfully sent the mail'
		except:
			print "failed to send mail"

