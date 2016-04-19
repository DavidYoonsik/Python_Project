# -*- coding: utf-8 -*-

from datetime import datetime

from elasticsearch import Elasticsearch

class connect_elk():
    es = Elasticsearch();
    
    def get_data(self, ind, typ):
        data = self.es.search(index=ind, doc_type=typ)
        sizes = 10 #data['hits']['total']
        data = self.es.search(index=ind, size=sizes)
        
        for hit in data['hits']['hits']:
            print(hit["_source"])
            
    def create_index(self, ind, typ, doc):
        result = self.es.index(index=ind, doc_type=typ, body=doc)
        print(result['created'])
        
elk = connect_elk()

elk.get_data('facebook', 'fb')

