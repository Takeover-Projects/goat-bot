""" Quickstart script for InstaPy usage """

# imports
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace

#Add COmments here seperated by a ,
comments = ['Nice shot! @{}',
        'I love your profile! @{}',
        'Getting inspired by you @{}',
        ':raised_hands: Yes!',
        '@{} :heart::heart:',
        'Love your posts @{}',
        'Looks awesome @{}',
        'Getting inspired by you @{}',
        ':raised_hands: Yes!',
        '@{}:revolving_hearts::revolving_hearts:', '@{}:fire::fire::fire:',
        'Inspiring post!',
        'I can feel your passion @{} :muscle:']

# set workspace folder at desired location (default is at your home folder)
set_workspace(path=None)

# get an InstaPy session!
session = InstaPy()

with smart_run(session):
    # general settings
    session.set_dont_include(["friend1", "friend2", "friend3"])

    # activity
    #session.like_by_tags(["natgeo"], amount=10)

    # comment stuff
    session.set_do_comment(enabled=True, percentage=35)
    session.set_comments(comments)
    session.join_pods(topic='entertainment', engagement_mode='no_comments')
