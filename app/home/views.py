from flask import render_template
from flask_login import login_required
from .twitter_funcs import *
from . import home


@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="Welcome")


@home.route('/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    tweets = get_tweets()
    tweets_count = get_recent_tweets_count(tweets)
    tweets_good, good_tweets_count, bad_tweets_count = get_tweet_sentiment(tweets)

    if tweets_good:
        text_type = "text-success"
    else:
        text_type = "text-danger"

    return render_template('home/dashboard.html', title='Dashboard', tweets_count=tweets_count, text_type=text_type,
                           good_count=good_tweets_count, bad_count=bad_tweets_count)


@home.route('/tweets')
@login_required
def tweets():
    tweets = get_tweets()
    return render_template('home/tweets.html', title='Tweets', tweets=tweets)


@home.route('/tweets/<technical_or_not>')
def toggle_tweets(technical_or_not):
    if technical_or_not == "technical":
        is_technical = True
    elif technical_or_not == "not-technical":
        is_technical = False

    tweets = get_tweets(is_technical)

    return render_template('home/tweets.html', title='Tweets', tweets=tweets)
