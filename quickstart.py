import random
from instapy import InstaPy
from instapy import smart_run

# get a session!
session = InstaPy(username='amazingescaperoompromos', password='2211530ron',
                  headless_browser=False)

# easier one 

# let's go! :>
with smart_run(session):
    hashtags = ['axethrowing', 'axes', 'beer',
                'axe',
                'hatchet', 'nj', 'philly',
                'axelife', 'craftbeer',
                'newjersey', 'brooklyn', 'monmouthcounty', 'statenisland'
                ]
    random.shuffle(hashtags)
    my_hashtags = hashtags[:10]

    # general settings
    session.set_dont_like(['sad', 'rain', 'depression'])
    session.set_do_follow(enabled=True, percentage=10, times=2)
    session.set_do_comment(enabled=True, percentage=80)
    session.set_comments([
                             u':fire: :heart_eyes: ',
                             u'Great Photo! ' ,
                             u'Sick!! :heart_eyes:' ,
			     u'You have a cool page' , 	
                             ],
                         media='Photo')
    session.set_do_like(True, percentage=70)
    session.set_delimit_liking(enabled=True, max_likes=200, min_likes=0)
    session.set_delimit_commenting(enabled=True, max_comments=20, min_comments=0)
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    max_followers=3000,
                                    max_following=2000,
                                    min_followers=100,
                                    min_following=50)

    session.set_quota_supervisor(enabled=True,
                                 sleep_after=["likes", "follows"],
                                 sleepyhead=True, stochastic_flow=True,
                                 notify_me=True,
                                 peak_likes_hourly=200,
                                 peak_likes_daily=1000,
                                 peak_comments_hourly=61,
                                 peak_comments_daily=250,
                                 peak_follows_hourly=200,
                                 peak_follows_daily=None)

    session.set_user_interact(amount=1, randomize=False, percentage=40)

    # activity
    session.like_by_tags(my_hashtags, amount=60, media=None)
    session.unfollow_users(amount=500, InstapyFollowed=(True, "nonfollowers"),
                           style="FIFO",
                           unfollow_after=12 * 60 * 60, sleep_delay=501)
    session.unfollow_users(amount=500, InstapyFollowed=(True, "all"),
                           style="FIFO", unfollow_after=24 * 60 * 60,
                           sleep_delay=501)

    """ Joining Engagement Pods...
    """
    session.join_pods(topic='sports', engagement_mode='no_comments')
