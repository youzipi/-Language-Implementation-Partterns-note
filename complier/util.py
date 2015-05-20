# -*- coding: utf-8 -*- 
# __author__ = 'youzipi'


class Enum:
    def __init__(self, *arguments):
        #print(arguments)
        for item in arguments:
            setattr(self, item.upper(), item)
types = Enum("others", "chars", "keywords", "numbers", "operator", "lbreak", "rbreak", "comma")
