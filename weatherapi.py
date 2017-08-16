from __future__ import unicode_literals, print_function
import urllib, json

import twitter

def tempbyID(ID):
    baseurl = "https://query.yahooapis.com/v1/public/yql?"
    yql_query = "select item.condition.temp from weather.forecast where woeid ={}".format(ID)
    yql_url = baseurl + urllib.request.urlencode({'q': yql_query}) + "&format=json"
    result = urllib.request.urlopen(yql_url).read()
    data = json.loads(result)
    print(data)
    print(data['query']['results'])
    tempget = data['query']['results']
    print(tempget['channel']['item']['condition']['temp'])
    return tempget['channel']['item']['condition']['temp']