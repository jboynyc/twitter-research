## tools

* `query_backwards.py` uses the [REST API](https://dev.twitter.com/rest/reference/get/search/tweets) 
to track a query back as far as possible.
* `track_stream.py` uses the [Streaming API](https://dev.twitter.com/streaming/overview).

Run from the command line providing a keyword/query.

```
$ python3 track_stream.py \#icantbreathe
```

## requirements

* [MongoDB](https://www.mongodb.org/)
* [python-requests](https://pypi.python.org/pypi/requests)
* [python-requests-oauthlib](https://pypi.python.org/pypi/requests-oauthlib)
* [pymongo](https://pypi.python.org/pypi/pymongo)
* [pyyaml](https://pypi.python.org/pypi/PyYAML)

Developed with Python 3. Probably won't work with Python 2.7 unless backported.

## template for YAML files in `tokens/`

```yaml
api_key: xxxxxxxxxxxxxxxxxxxxxxxxx
api_secret: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
token: xxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
token_secret: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

**Disclaimer:** This is a *hack* and there are likely existing tools that do a better job.
