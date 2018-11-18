#!/usr/bin/env python

import sys
from itertools import groupby

class Reducer:
    
    def __init__(self, stream):
        self.stream  = stream
    
    def emit(self, key, value):
        
        if value != '' and value != '\t' and value != '\n' and \
        value != '\t\n' and key != '' and key != '\t' \
        and key != '\n' and key != '\t\n':
            sys.stdout.write('{}\t{}\n'.format(key, value))
    
    def reduce(self):
        for key, group in groupby(self, lambda x: x[0]):
            indices = []
            for i in group:
                indices.append(i[1])
            indices = ",".join(indices)
            self.emit(key, indices)
    
    def __iter__(self):
        for line in self.stream:
            key, val = line.replace('\n', '').split('\t')
            yield(key,val)

if __name__ == '__main__': 
    reducer = Reducer(sys.stdin)
    reducer.reduce()