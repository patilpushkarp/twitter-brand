import traceback
import pandas as pd
from datetime import datetime, timedelta
import snscrape.modules.twitter as sntwitter


def scrape(x, dates):
    try:
        tweets_list= []
        query = f"starbucks since:{dates[x]} until:{dates[x+1]}"
        print(f"Running query: '{query}'")
        for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
            td = get_schema(tweet)
            tweets_list.append(td)
        n_tweets = len(tweets_list)
        print(f"Tweets scrapped: {n_tweets}")
        df = pd.DataFrame(tweets_list)
        df.to_csv(f'./../data/starbucks/{dates[x]}.csv')
        print("\n")
    except:
        traceback.print_exc()


def get_schema(tweet):
    return {   
        'tweet': tweet.content,
        'conversation_id': tweet.conversationId,
        'date':tweet.date,
        'hashtags':tweet.hashtags,
        'id':tweet.id,
        'inReplyToTweetId':tweet.inReplyToTweetId,
        'reply_to':tweet.inReplyToUser,
        'language':tweet.lang,
        'likes_count':tweet.likeCount,
        'media':tweet.media,
        'mentions':tweet.mentionedUsers,
        'quote_count':tweet.quoteCount,
        'quoted_tweet':tweet.quotedTweet,
        'replies_count':tweet.replyCount,
        'retweets_count':tweet.retweetCount,
        'link':tweet.url,
        'followers_count':tweet.user.followersCount,
        'following_count':tweet.user.friendsCount,
        'favourites_count':tweet.user.favouritesCount,
        'user_status_count':tweet.user.statusesCount,
        'location':tweet.user.location,
        'name':tweet.user.displayname,
        'description':tweet.user.description,
        'verified':tweet.user.verified,
        'url':tweet.user.linkUrl,
        'user_id':tweet.user.id,
        'username':tweet.user.username}