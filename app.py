import tweepy
import os

bearer_token = os.getenv("BEARER_TOKEN")
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# V1 api authentication
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# V2 api authentication
client = tweepy.Client(
    bearer_token,
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)


# Make a tweet with only text
def text_tweet():  # POST request
    text = "These is automated tweet"
    return client.create_tweet(text=text)


# print(text_tweet())


def tweet_with_photo():  # POST request
    text = "#switzerland"
    image_id = api.simple_upload(filename="swiz.jpg").media_id
    return client.create_tweet(text=text, media_ids=[image_id])


# print(tweet_with_photo())

def delete_tweet():  # DELETE request
    return client.delete_tweet(id=1820468627574812894)


# print(delete_tweet())


def get_info_by_username():
    return client.get_user(username='dinesh_125')


# print(get_info_by_username())


def get_following_list():  # GET request
    return client.get_users_following(id=1820422094535938048)


print(get_following_list())
