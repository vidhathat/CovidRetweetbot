import tweepy
import time

auth = tweepy.OAuthHandler("API_KEY", "API_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

api = tweepy.API(auth)

def check_mentions(api,keyword):
    for tweet in tweepy.Cursor(api.mentions_timeline).items():
        if tweets.in_reply_to_status_id is not None:
            continue
        if any(keyword in tweet.text.lower() for keyword in keywords):
            if not tweet.retweeted:
                tweet.retweet()
            
    return "Done."

def main():
    print("Now working")
    while True:
        check_mentions(api, ["#sos","remdesivir","bed","oxygen","icu","sos","o2","hospital","covid-19","patient","covid","hyd","hyderabad","#covid","#hyd","#urgent"])
        time.sleep(60)

if __name__== "__main__":
    main()      


    

