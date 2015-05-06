import string

chars = string.ascii_letters
break_char = "()[]{}"
space = " "
keywords = ["int","main","return"]
numbers = "01234546789"
comma = ",;"
operator = "+-*/="

type = ["keywords","chars","numbers","operator","break","comma"]


class Test:
    temp = ""
    status = ""
    list = []
    filename = ""
    lines = []
    
    
    def __init__(self,filename):
        self.file = open(filename)
        self.lines =self.file.readlines()
        print self.lines


    def add_item(self,item):
        print item
        #print type(list)
        #print list
        self.list.append((item,"chars"))
        temp = ""
        status = 0
        
    def clear(self):
        self.temp = ""
        self.status = 0

    def process(self):
        print list
        for l in self.lines:
            print l
            for i in l:
                if(i == space):
                    if (status != 0):
                        self.add_item(self.temp)
                        self.clear()
                elif( i in chars):
                    status = 1
                    self.temp += i
                elif( i in break_char):
                    if (status == 1):
                        self.add_item(self.temp)
                        self.clear()
                    self.list.append((i,"break"))
                elif(i in comma):
                    self.list.append((i,"comma"))
                elif(i in numbers):
                    self.list.append((i,"numbers"))
                elif(i in operator):
                    self.list.append((i,"operate"))
        #print type(list)
        for i in self.list:
            print i
            
test = Test("D:/Desktop/test.txt")
test.process()
