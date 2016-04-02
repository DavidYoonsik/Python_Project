# -*- coding: ms949 -*- 

from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch();

doc = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
    'timestamp': datetime.now()
}

res = es.index(index="test-index", doc_type='tweet', id=1, body=doc)
# create index, meaning make room for the data which will come to
print(res['created'])

res = es.search(index="test-index", body={"query": {"match_all": {}}})
print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])
    
res = es.search(index="books", body={"query": {"match_all": {}}})
print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
    print hit['_source']['author']