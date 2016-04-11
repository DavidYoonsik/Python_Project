from datetime import datetime

from elasticsearch import Elasticsearch

es = Elasticsearch();

doc = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
    'timestamp': datetime.now()
    
}

#res = es.index(index="test-index", doc_type='tweet', id=1, body=doc)

# create index, meaning make room for the data which will come to
#print(res['created'])

test = es.search(index=['movies'],doc_type=['movie'])
sizes = test['hits']['total']

res = es.search(index="movies", size=sizes) #body={"query": {"match_all": {}}}

print("Got %d Hits:" % res['hits']['total'])
for hit in res['hits']['hits']:
    print(hit["_source"])
    fo = open("log.txt", "wb")
    fo.write(hit["_source"]);