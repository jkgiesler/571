from twython import TwythonStreamer
from datetime import datetime

'''
a much simpler interface for searching the twitter stream based on a query (labeled as track = )
note here that a comma represents OR if I were to use a space to seperate hashtags it would be considerd and AND
'''
#https://twython.readthedocs.org/en/latest/usage/streaming_api.html

class TweetStreamer(TwythonStreamer):
	def on_success(self,data):
		if 'text' in data:
			outfile = open("streaming.txt","at")
			print(data['text'].encode('utf-8'))
			print(str(datetime.now()), file = outfile)
			print(data['text'].encode('utf-8'), file = outfile)
			outfile.close()
		def on_error(self,status_code,data):
			print(status_code)
			self.disconnect

APP_KEY = #NOTE TO SELF: THESE KEYS ARE PRIVATE. DO NOT BE AN IDIOT AND POST THIS CODE ON GITHUB
APP_SECRET = 
TWITTER_ACCESS_TOKEN = 
TWITTER_ACCESS_TOKEN_SECRET = 

streamer = TweetStreamer(APP_KEY,APP_SECRET,
	TWITTER_ACCESS_TOKEN,
	TWITTER_ACCESS_TOKEN_SECRET)

streamer.statuses.filter(track = '#climatechange,#globalwarming')
