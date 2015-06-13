# -*- coding: utf-8 -*- 
# __author__ = 'youzipi'


class Enum:
    def __init__(self, list):
        #print(arguments)
        self.OTHERS = "others"
        self.CHARS = "chars"
        self.KEYWORDS = "keywords"
        self.NUMBERS = "numbers"
        self.OPERATOR = "operator"
        self.LBREAK = "lbreak"
        self.RBREAK = "rbreak"
        self.COMMA = "comma"
        self.SEMICOLON = "semicolon"
        self.EQUAL = "equal"
        for item in list:
            setattr(self, item.upper(), item)
            # print item.upper()
            print item
types = Enum(["others", "chars", "keywords", "numbers", "operator", "lbreak", "rbreak", "comma", "semicolon", "equal"])

print types.OTHERS
