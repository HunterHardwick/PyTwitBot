# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
import credentials, twitter

def tweetit(text):
    api = credentials.apiget()
    status = api.PostUpdate(text)
def mentionUpdate():
    api = credentials.apiget()
    mentions = api.GetMentions()
    stuff = {}
    for item in mentions:
         stuff[item.id] = item.text
    return stuff


# print(api.users)
# users = api.GetFriends()
# api.GetFavorites(user_id=)
# print(users)
# print([u.name for u in users])



