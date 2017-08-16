# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
import credentials,darkAPI,weatherapi,requests, re,twitterhandling,json
#APIcall: api = credentials.apiget()

def core():

    api = credentials.apiget()
    mentions = api.GetMentions()
    stuff = {}

    for item in mentions:
        flag = 0
        for word in item.text.split():
            print(word)
            if "up" in word:
                print("caught " + word)
                stuff[item.id] = item.text
                flag = 1
                break

        path = credentials.historypathget() #File Location for history json file

        with open(path, "w") as fp:
            json.dump(stuff, fp)


if __name__ == '__main__':
    core()

# https: // github.com / bear / python - twitter