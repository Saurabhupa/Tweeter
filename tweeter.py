import tweepy

# Twitter API Keys and Tokens
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Authenticate with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Function to tweet
def tweet(status):
    try:
        api.update_status(status)
        print(f"Tweeted: {status}")
    except tweepy.TweepError as e:
        print(f"Error: {e.reason}")

# Function to retweet
def retweet(username):
    try:
        latest_tweet = api.user_timeline(screen_name=username, count=1)[0]
        api.retweet(latest_tweet.id)
        print(f"Retweeted the latest tweet from {username}")
    except tweepy.TweepError as e:
        print(f"Error: {e.reason}")

# Main program
if __name__ == "__main__":
    command = input("Enter a command (-tweet or -retweet): ")
    
    if command == "-tweet":
        tweet_content = input("Enter your tweet: ")
        tweet(tweet_content)
    elif command == "-retweet":
        user_to_retweet = input("Enter the username to retweet from: ")
        retweet(user_to_retweet)
    else:
        print("Invalid command. Use -tweet or -retweet.")
