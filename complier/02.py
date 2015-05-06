import string

chars = string.ascii_letters
break_char = "()[]{}"
space = " "
keywords = ["int", "main", "return"]
numbers = "01234546789"
comma = ",;"
operator = "+-*/="

type = ["keywords", "chars", "numbers", "operator", "break", "comma"]

temp = ""
status = 0
list = []


file = open("D:/Desktop/test.txt")
lines = file.readlines()
print "lines=", len(lines)
new_lines = []
for line in lines:
    line = line.strip('\n')
    new_lines.append(line)
    print line
lines = new_lines


def add_item():
    global temp, status
    print "temp", temp
    list.append((temp, type[status]))
    temp = ""
    status = 0


def clear():
    temp = ""
    status = 0


def white_space():
    global l



for l in lines:
    print l
    #i = 0
    #for index in range(len(l)):
    for i, c in enumerate(l):
        if c == space:
            if status != 0:
                add_item()
        elif c in chars:
            # temp = c
            while(l[i] in chars):
                temp += l[i]
                i += 1
            add_item()

        elif c in break_char:
            if status != 0:
                add_item()
            list.append((c, "break"))
        elif c in comma:
            list.append((c, "comma"))
        elif c in numbers:
            list.append((c, "numbers"))
        elif c in operator:
            list.append((c, "operate"))

print list
for i in list:
    print i


foo="abcdef"
index=0
while(index < len(foo)):
    print foo[index]
    index += 2
