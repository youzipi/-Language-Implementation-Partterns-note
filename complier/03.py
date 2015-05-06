import string

chars = string.ascii_letters
break_char = "()[]{}"
space = " "
keywords = ["int", "main", "return"]
numbers = "01234546789"
numbers2 = ".01234546789"
comma = ",;"
operator = "+-*/="

type = ["others", "chars", "keywords", "numbers", "operator", "break", "comma"]

temp = ""
status = 0
list = []

file = open("D:/Desktop/LIP/complier/test.txt")
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
    list.append((temp, type[status]))
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
        if c == space:
            #if status != 0:
               # add_item()
            index += 1
            continue
        elif c in chars:
            temp = c
            status = 1
            index += 1
            while l[index] in chars:
                temp += l[index]
                index += 1
            add_item()
            continue
        elif c in numbers:
            #list.append((c, "numbers"))
            temp = c
            status = 3
            index += 1
            while l[index] in numbers2:
                temp += l[index]
                index += 1
            add_item()
            continue
        elif c in break_char:
            if status != 0:
                add_item()
            list.append((c, "break"))
        elif c in comma:
            list.append((c, "comma"))
        elif c in operator:
            list.append((c, "operator"))
        index += 1

print list
for i in list:
    print i

foo = "abcdef"
index = 0
while index < len(foo):
    print foo[index]
    index += 2
