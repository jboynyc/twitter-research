import json
import requests
from glob import glob
from random import shuffle
from yaml import load as yaml_load
from requests_oauthlib import OAuth1
from urllib.parse import urlencode

SEARCH_URL = 'https://api.twitter.com/1.1/search/tweets.json?'
STREAM_URL = 'https://stream.twitter.com/1.1/statuses/filter.json'
VERIFY_URL = 'https://api.twitter.com/1.1/account/verify_credentials.json?'

def twitter_track(keywords, token, params={}):
    params['track'] = keywords
    r = requests.post(STREAM_URL, data=params, auth=token, stream=True)
    return r

def twitter_search(query, token, max_id=None, since='2006-03-21', count=100, params={}):
    params['q'] = query+' since:'+since
    params['count'] = count
    if max_id:
        params['max_id'] = max_id
    r = requests.get(SEARCH_URL+urlencode(params), auth=token)
    if r.status_code < 400:
        j = json.loads(r.text)
        if 'statuses' in j.keys() and len(j['statuses']):
            return j['statuses'], min([t['id'] for t in j['statuses']])

def get_valid_token(tokendir):
    tokenfiles = glob(tokendir+'*.yaml')
    shuffle(tokenfiles)
    for f in tokenfiles:
        token = _load_token(f)
        if _verify_token(token):
            return token
            break
    return None

def _load_token(file):
    with open(file) as tokenfile:
        token = yaml_load(tokenfile)
    return OAuth1(token['api_key'],
            client_secret = token['api_secret'],
            resource_owner_key = token['token'],
            resource_owner_secret = token['token_secret'])

def _verify_token(oauth):
    params = {'skip_status':True, 'include_entities':False}
    r = requests.get(VERIFY_URL+urlencode(params), auth=oauth)
    return r.status_code == 200

def bold(str):
    BOLD_START = '\033[1m'
    BOLD_END = '\033[0m'
    return BOLD_START + str + BOLD_END

def format_collection_name(str):
    return str.replace('#', 'hashtag ').replace(' ', '_').replace('"','').lower()

