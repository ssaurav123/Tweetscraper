try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API
ACCESS_TOKEN = '3228002139-6mBm4NQ8oCTeAwOAXzYZ2mhanWsbNIiHxj4m74z'
ACCESS_SECRET = '4PVzELP3qxTAod2O2l6qSBVecfwNN7M0Rhe1WJwWLJCY0'
CONSUMER_KEY = 'zK842KgrvES47wtIZUDJNPy2N'
CONSUMER_SECRET = '4TxKLcVCr6rtQ4d8TKXtWD4ZLcjEvXOPVxoBRPq3Dnr6mmJCHV'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
t = raw_input('Enter the name of topic')
iterator = twitter_stream.statuses.filter(track=t,result_type='recent', language="en")

# Print each tweet in the stream to the screen
# Here we set it to stop after getting 1000 tweets.
# You don't have to set it to stop, but can continue running
# the Twitter API to collect data for days or even longer.
tweet_count = 100
for tweet in iterator:
    tweet_count -= 1
    # Twitter Python Tool wraps the data returned by Twitter
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
    print json.dumps(tweet)

    # The command below will do pretty printing for JSON data, try it out
    # print json.dumps(tweet, indent=4)

    if tweet_count <= 0:
        break
