## tools

* `query_backwards.py` uses the [REST API](https://dev.twitter.com/rest/reference/get/search/tweets) 
to track a query back as far as possible.
* `track_stream.py` uses the [Streaming API](https://dev.twitter.com/streaming/overview).

Run from the command line providing a keyword/query.

```
$ python3 track_stream.py \#icantbreathe
```

## requirements

* MongoDB
* python-requests
* python-requests-oauthlib
* pymongo
* pyyaml

Developed with Python 3. Probably won't work with Python 2.7 unless backported.

## template for YAML files in `tokens/`

```yaml
api_key: xxxxxxxxxxxxxxxxxxxxxxxxx
api_secret: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
token: xxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
token_secret: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

## keeping your collection deduplicated

Sometimes the script will grab the same tweet twice. To make sure it doesn't get stored a second time, run this:

```
$ mongo MY_DB --eval 'db.MY_COLLECTION.ensureIndex( {"id": 1}, {unique: true, dropDups: true} )'
```

(Obviously replace MY_* with the appropriate values.)

See [Create a Unique Index](http://docs.mongodb.org/manual/tutorial/create-a-unique-index/) in the MongoDB manual.

---

**Disclaimer:** This is a *hack* and there are likely existing tools that do a better job.
