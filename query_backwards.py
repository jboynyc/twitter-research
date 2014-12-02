import sys
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from utils import \
    get_valid_token, twitter_search, bold, format_collection_name

tokens = 'tokens/'
DB = MongoClient().twitter_experiment_1

def loop(query, token, collection, oldmax=None):
    tweets, newmax = twitter_search(query, token, max_id=oldmax)
    if oldmax: print('storing',len(tweets),'tweets since',oldmax)
    for t in tweets:
        try:
            collection.insert(t)
        except DuplicateKeyError:
            print('NOTE: tweet already exists in collection')
            pass
    if not oldmax or newmax < oldmax:
        print('running with max_id=',newmax)
        loop(query, token, collection, newmax)

if __name__ == '__main__':
    arg = sys.argv[1:]
    if len(arg) < 1:
        raise 
    query = ' '.join(arg)
    api_token = get_valid_token(tokens)
    if api_token:
        collection_name = format_collection_name(query)
        print('running for query', bold(query), 'and storing in collection', bold(collection_name))
        loop(query, api_token, DB[collection_name])
    else:
        print('No valid API token available in {}.'.format(tokens))

