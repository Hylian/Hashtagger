#! /usr/bin/env python

import sys
import tweepy

consumer_key = raw_input('Consumer Key:')
consumer_secret = raw_input('Consumer Secret:')
access_key = raw_input('Access Key:')
access_secret = raw_input('Access Secret:')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
            print status.text

    def on_error(self, status_code):
            print >> sys.stderr, 'Encountered error with status code:', status_code
            return True # Don't kill the stream

    def on_timeout(self):
            print >> sys.stderr, 'Timeout...'
            return True # Don't kill the stream

sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
sapi.filter(languages=['en'], track=['a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'])

