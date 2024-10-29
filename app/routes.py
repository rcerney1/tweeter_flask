from flask import Blueprint, render_template, redirect, url_for, request, flash
import random
from .tweets import tweets
from .form.form import TweetForm

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    tweet = random.choice(tweets)
    return render_template('index.html', tweet=tweet)

@bp.route('/feed')
def feed():
    return render_template('feed.html', tweets=tweets)

@bp.route('/new', methods=['GET', 'POST'])
def new_tweet():
    form = TweetForm()

    if form.validate_on_submit():
        new_tweet = {
            "id": len(tweets) + 1,
            "author": form.author.data,
            "date": "now idk",
            "tweet": form.tweet.data,
            "likes": 0
        }
        tweets.append(new_tweet)
        return redirect(url_for('main.feed'))
    return render_template('new_tweet.html', form=form)
