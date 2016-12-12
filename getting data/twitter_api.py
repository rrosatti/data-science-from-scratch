import requests, json
from twython import Twython, TwythonStreamer
from collections import Counter

with open('C:/Users/rodri/OneDrive/Documentos/twitter_credentials.json') as data_file:
	data = json.load(data_file)

CON_KEY = data['con_key']
CON_SECRET = data['con_secret']
ACC_TOKEN = data['access_token']
ACC_SECRET = data['access_secret']

'''
# Simple example using only Twython Class
twitter = Twython(KEY, SECRET)

# search for tweets containing the phrase 'data science'
for status in twitter.search(q='"data science"')['statuses']:
	user = status['user']['screen_name'].encode('utf-8')
	text = status['text'].encode('utf-8')
	print user, ":", text
	print
# the 'encode' is used to deal with Unicode characters the tweets may contain
'''

tweets = []

class MyStreamer(TwythonStreamer):

	def on_success(self, data):
		# data will be a Python dict representing a tweet

		# here we only will get English-language tweets
		if data['lang'] == 'en':
			tweets.append(data)
			print 'received tweet #', len(tweets)

		# stop at 50 tweets
		if len(tweets) >= 50:
			self.disconnect()

	def on_error(self, status_code, data):
		print status_code, data
		self.disconnect()


stream = MyStreamer(CON_KEY, CON_SECRET, ACC_TOKEN, ACC_SECRET)

# starts consuming public statuses that contain the keyword 'data'
stream.statuses.filter(track='data')

# we could also start consuming a sample of "all" public statuses using: stream.statuses.sample()

# finding the most common hashtags
top_hashtags = Counter(hashtag['text'].lower() for tweet in tweets for hashtag in tweet['entities']['hashtags'])
print top_hashtags.most_common(5)