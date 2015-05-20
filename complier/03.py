import string
from util import Enum

chars = string.ascii_letters
break_char = "()[]{}"
lbreak_char = "([{"
rbreak_char = "0]}"
space = " "
keywords = ["int", "main", "if", "else", "return"]
numbers = "01234546789"
numbers2 = ".01234546789"
comma = ",;"
operator = "+-*/="

types = ["others", "chars", "keywords", "numbers", "operator", "lbreak", "rbreak", "comma"]
#types = Enum("others", "chars", "keywords", "numbers", "operator", "lbreak", "rbreak", "comma")

temp = ""
status = 0
list = []

file = open("D:/Desktop/LIP/complier/test.c")
lines = file.readlines()
print "lines=", len(lines)
new_lines = []
for line in lines:
    line = line.strip('\n\t')
    new_lines.append(line)
    print line
lines = new_lines


def add_item():
    global temp, status
    print "temp", temp
    if temp in keywords:
        status = 2

    list.append((temp, types[status]))
    temp = ""
    status = 0


def clear():
    temp = ""
    status = 0


def white_space():
    global l


for l in lines:
    print "l=", l
    length = len(l)
    index = 0
    while index < length:
        c = l[index]
        # if c == space:
        if c.isspace():
            #if status != 0:
               # add_item()
            index += 1
            continue
        # elif c in chars:
        elif c.isalpha():
            temp = c
            status = 1
            index += 1
            while l[index].isalnum() or l[index] == '_':
                temp += l[index]
                index += 1
            add_item()
            continue
        # elif c in numbers:
        elif c.isdigit():
            #list.append((c, "numbers"))
            temp = c
            status = 3
            index += 1
            while l[index] in numbers2:
                temp += l[index]
                index += 1
            add_item()
            continue
        elif c in lbreak_char:
            if status != 0:
                add_item()
            list.append((c, "lbreak"))
        elif c in rbreak_char:
            if status != 0:
                add_item()
            list.append((c, "rbreak"))
        elif c in comma:
            list.append((c, "comma"))
        elif c in operator:
            list.append((c, "operator"))
        index += 1

print list
for i in list:
    print i


