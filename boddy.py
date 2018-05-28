import tweepy
from tweepy.streaming import StreamListener

#Consumer Keys used, which are no longer valid, and cannot be used
consumerKey=""
consumerSecret=""
accessToken=""
accessSecret=""
#Authenticate will connnect to twitter to verify the API using the tweepy library (followed from tutorial)
#link to source: https://tweepy.readthedocs.io/en/v3.5.0/auth_tutorial.html

def authenticate(consumerKey,consumerSecret,accessToken,accessSecret):
    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(accessToken, accessSecret)
    api = tweepy.API(auth)
    try:
        redirect_url = auth.get_authorization_url()
    except tweepy.TweepError:
        print('Error! Failed to get request token.')
    auth.access_token=accessToken
    auth.access_token_secret=accessSecret
    api = tweepy.API(auth)
    #get the list of favorites from my account using the API
    timeline = tweepy.Cursor(api.favorites).items()
    #Loop to destroy tweets
    #Referenced from here: http://www.mathewinkson.com/2015/03/delete-old-tweets-selectively-using-python-and-tweepy

    for tweet in timeline:
        api.destroy_favorite(tweet.id)
 #Call the Function       
authenticate(consumerKey,consumerSecret,accessToken,accessSecret)
    