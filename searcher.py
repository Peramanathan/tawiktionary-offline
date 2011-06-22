#!/usr/bin/python
# -*- encoding: UTF-8 -*-
'''
The text entered during the searching should be parsed into search objects for
the Whoosh library.

This file recieves the text entered and parses into searchable objects and
performs search operations.
'''
import re

from whoosh import index
from whoosh.fields import *
from whoosh.qparser import QueryParser

def search_for(text):
    ''' This function gets the search query string and returns the list of
    dictionary of the hits (file_name and titles) '''
    ix = index.open_dir("indexdir")
    res = []
    with ix.searcher() as searcher:
        query = QueryParser("word", ix.schema).parse(unicode(text))
        results = searcher.search(query, limit=None)
        for result in results:
            temp = {}
            temp['meaning'] = result['meaning']
            temp['word'] = result['word']
            res.append(temp)
    return res

def get_markup(index_text):
    ''' The get_markup function checks wether the index contains full wiki text
    or the name of the file which contains wiki text and returns the wiki text
    in first case. It obtains the wikitext from the file and returns it in
    second case.'''
    filexp = re.compile("chunk-[0-9]{1,}.xml.bz2")
    if filexp.match(index_text):
        #parse the file and return wiki text
        print "Contains File Name"
        return index_text
    else:
        return index_text
    

if __name__ == "__main__":
    searchterm = raw_input("Enter the Search Term: ")
    r = search_for(searchterm)
    for rs in r:
        print str(r.index(rs)),unicode(rs['word'])
    choice = int(raw_input('Enter your option: '))
    opt =  r[choice]
    print get_markup(opt['meaning'])
        
        

