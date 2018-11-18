#! /usr/bin/env python

import sys

class Mapper:

    def __init__(self, stream):
        self.stream  = stream
    
    def emit(self, key, value=1):
        sys.stdout.write('{}\t{}\n'.format(key, value))
    
    def map(self):
        for palabra in self:            
            aux_split = palabra.replace(" 	 ", "\t").split('\t')
            numero = aux_split[0].strip()
            letras = aux_split[1].strip().split(',')
            
            for letra in letras:
                self.emit(letra,numero)

    def __iter__(self):
        for linea in self.stream:
            yield linea#[:-1]
            
if __name__ == "__main__": 
    mapper = Mapper(sys.stdin)
    mapper.map() 