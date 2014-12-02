import sys
import json
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from utils import \
    get_valid_token, twitter_track, bold, format_collection_name

tokens = 'tokens/'
DB = MongoClient().twitter_experiment_1

if __name__ == '__main__':
    arg = sys.argv[1:]
    if len(arg) < 1:
        raise 
    kw = ' '.join(arg)
    api_token = get_valid_token(tokens)
    if api_token:
        collection_name = format_collection_name(kw)
        print('tracking keyword', bold(kw), 'and storing in collection', bold(collection_name))
        for tweet in twitter_track(kw, api_token).iter_lines():
            if tweet:
                try:
                    DB[collection_name].insert(json.loads(tweet.decode()))
                except DuplicateKeyError:
                    print('NOTE: tweet already exists in collection')
                    pass
    else:
        print('No valid API token available in {}.'.format(tokens))

