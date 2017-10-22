# -*- coding: utf-8 -*-
import credentials
import json
import tweepy

u'''
Credential has the following values.

CONSUMER_KEY = '***'
CONSUMER_SECRET_KEY = '***'
'''

def get_client():
    try:
        with open('.token.json', 'r') as f:
            token = json.load(f)
        auth = tweepy.OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET_KEY)
        auth.set_access_token(token['ACCESS_TOKEN'], token['ACCESS_TOKEN_SECRET'])
    except FileNotFoundError as e:
        auth = authorize()
    except KeyError as e:
        auth = authorize()

    api = tweepy.API(auth)
    return api


def authorize():
    auth = tweepy.OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET_KEY)

    # get access token from the user and redirect to auth URL
    try:
        redirect_url = auth.get_authorization_url()
    except tweepy.TweepError:
        print('Error! Failed to get request token.')
        return None
    print('Open the following URL in the browser. ')
    print(redirect_url)

    # ask user to verify the PIN generated in broswer
    verifier = input('Input PIN: ').strip()
    try:
        auth.get_access_token(verifier)
    except tweepy.TweepError:
        print('Error! Failed to get access token.')
        return None

    token = {
        'ACCESS_TOKEN': auth.access_token,
        'ACCESS_TOKEN_SECRET': auth.access_token_secret,
    }
    with open('.token.json', 'w') as f:
        json.dump(token, f)
    return auth
