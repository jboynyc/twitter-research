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
