# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function


def darkurl(key,coordstring,queries):
    url = "https://api.darksky.net/forecast/"
    url += key
    url += "/"
    url += coordstring
    url += "/?exclude=[{}]".format(queries)
    url +=  "&format=json"
    return url
