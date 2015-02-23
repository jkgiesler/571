from twython import Twython
import time

'''
searches the not streaming part of twitter for a specific hashtag -- heavily relies on stackoverflow link
for logic which allows more than one query. I guess it's based on being able to call next page function?
'''



APP_KEY =  #NOTE TO SELF: THESE KEYS ARE PRIVATE. DO NOT BE AN IDIOT AND POST THIS CODE ON GITHUB
APP_SECRET = 
TWITTER_ACCESS_TOKEN = 
TWITTER_ACCESS_TOKEN_SECRET = 

def get_tweets_from_hastag(hashtag,max_count,write = True):
	# http://stackoverflow.com/questions/19320197/twython-search-api-with-next-results
	tweets = []
	max_attempts = 50
	twitter = Twython(app_key = APP_KEY,
	app_secret = APP_SECRET, 
	oauth_token = TWITTER_ACCESS_TOKEN, 
	oauth_token_secret	= TWITTER_ACCESS_TOKEN_SECRET)
	twitter.verify_credentials()

	for i in range(0,max_attempts):
		if(max_count < len(tweets)):
			break

		if(i == 0):
			results = twitter.search(q=hashtag,count = '100') #get initial query

		else:
			results = twitter.search(q=hashtag,include_entities='true',max_id = next_max_id) #try to get next page of tweets

		for result in results['statuses']:
			tweet_text = result['text']
			tweets.append(tweet_text)

		try:
			next_results_url_params = results['search_metadata']['next_results']
			next_max_id = next_results_url_params.split('max_id=')[1].split('&')[0]
		except:
			break

	if(write):
		file_out = open(hashtag[1:]+".txt",'wt')
		tweets = list(set(tweets))
		for i in tweets:
			print(i.encode('utf-8').strip(),file= file_out)
		file_out.close()
	return tweets


##you have to wait here 15 minutes due to twitter limititations
##dont wanna get blacklisted :/
get_tweets_from_hastag("#ammo",1000)
print("waiting")
time.sleep(60*15)
get_tweets_from_hastag("#glock",1000)
print("waiting")
time.sleep(60*15)
get_tweets_from_hastag("#firearms",1000)
print("waiting")
time.sleep(60*15)
get_tweets_from_hastag("#NRA",1000)
print("waiting")
time.sleep(60*15)
get_tweets_from_hastag("#2nd",1000)
print("waiting")
time.sleep(60*15)
get_tweets_from_hastag("#guncontrol",1000)
print("waiting")
time.sleep(60*15)
get_tweets_from_hastag("#gunrights",1000)
print("waiting")
time.sleep(60*15)
get_tweets_from_hastag("#shooting",1000)
print("waiting")
time.sleep(60*15)
get_tweets_from_hastag("#wakingup",1000)
print("waiting")
time.sleep(60*15)
get_tweets_from_hastag("#evolution",1000)
print("waiting")
time.sleep(60*15)
get_tweets_from_hastag("#PERP",1000)
print("waiting")
time.sleep(60*15)
get_tweets_from_hastag("#OFFICER",1000)
print("waiting")
time.sleep(60*15)
get_tweets_from_hastag("#bullets",1000)