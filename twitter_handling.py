from TwitterSearch import *

consumer_key = "CONSUMER_KEY"
consumer_secret = "CONSUMER_SECRET"
access_token = "ACCESS_TOKEN"
access_token_secret = "ACCESS_TOKEN_SECRET"

twitter_api = TwitterSearch(consumer_key,
                            consumer_secret,
                            access_token,
                            access_token_secret)


def get_track_title(user_id):
    try:
        tuo = TwitterUserOrder(user_id)
        latest_tweets = twitter_api.search_tweets_iterable(tuo).get_tweets()
        latest_song_tweet = latest_tweets[0]['text']
        at_index = latest_song_tweet.find('@')
        hash_index = latest_song_tweet.find('#')
        if at_index == -1 and hash_index == -1:
            return latest_song_tweet[12:].replace(',', '').replace('&amp; ', '')
        elif (at_index != -1 and at_index < hash_index) or hash_index == -1:
            return latest_song_tweet[12: at_index - 1].replace(',', '').replace('&amp; ', '')
        else:
            return latest_song_tweet[12: hash_index - 1].replace(',', '').replace('&amp; ', '')

    except Exception as e:
        print("Some error occured... (twitter_handling.py): ", e)
