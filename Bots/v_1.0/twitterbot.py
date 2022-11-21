
import tweepy

# Variables that contains the credentials to access Twitter API
ACCESS_TOKEN = '1594434951113482241-bFcSbpO2mnKq4UaOWonFue9IYc5Lei'
ACCESS_SECRET = 'lJJBOwIRTnToV7PO9nIINqmQFQYFHVXHuj1tXOKCIHSqI'
CONSUMER_KEY = 'SGh0whNXZWmq6jf8xUV72KcHK'
CONSUMER_SECRET = 'fr68c6OoWVlyczgEOup4P84nUonApB2InjMjdUS59u7oJdygOt'


# Setup access to API
def connect_to_twitter_OAuth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth)
    return api


# Create API object
api = connect_to_twitter_OAuth()


# tweets from my stream
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
