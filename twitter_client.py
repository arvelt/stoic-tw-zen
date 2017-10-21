# -*- coding: utf-8 -*-
import credential

u'''
Credential has the following values.

CONSUMER_KEY = '***'
CONSUMER_SECRET_KEY = '***'
ACCESS_TOKEN = '***'
ACCESS_TOKEN_SECRET = '***'
'''

def get_client():
    import tweepy
    auth = tweepy.OAuthHandler(credential.CONSUMER_KEY, credential.CONSUMER_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    return api
