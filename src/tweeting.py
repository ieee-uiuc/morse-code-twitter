#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# morse-code-twitter

import twitter
from secrets import AuthKeys

t = twitter.Twitter(auth=twitter.OAuth(
    AuthKeys['token'], AuthKeys['token_secret'],
    AuthKeys['consumer_key'], AuthKeys['consumer_secret']))


def send_tweet(tweet):
    """ Given a tweet, tweet it. """
    print(tweet)
    t.statuses.update(status=tweet)


def main():
    """ Tweet an example tweet. """
    import sys

    if len(sys.argv) == 1:
        print('USAGE: ./tweeting.py YOUR TWEET')
        return

    tweet = ' '.join(sys.argv[1:])
    send_tweet(tweet)


if __name__ == '__main__':
    main()
