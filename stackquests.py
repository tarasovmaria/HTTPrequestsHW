from pprint import pprint

import requests


def get_questions():
    url = "https://api.stackexchange.com/2.3/questions?fromdate=1682294400&todate=1682553600&order=desc&sort=activity&tagged=Python&site=stackoverflow"
    resp = requests.get(url=url)
    for item in resp.json()['items']:
        pprint (item['title'])
get_questions()