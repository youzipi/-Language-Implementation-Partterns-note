# coding=utf-8
from util import Enum

break_char = "()[]{}"
lbreak_char = "([{"
rbreak_char = "0]}"
space = " "
keywords = ["int", "main", "if", "else", "return"]
numbers2 = ".01234546789"
comma = ","
semicolon = ";"
operator = "+-*/="
equal = "="

types = ["others", "chars", "keywords", "numbers", "operator", "lbreak", "rbreak", "comma", "semicolon", "equal"]
typess = Enum()


class Token(object):
    def __init__(self, value, token_type):
        self.type = token_type
        self.value = value

    def __str__(self):
        return "<%s : %s>" % (self.value, self.type)


class Lexer(object):
    def __init__(self, path):
        content = open(path)
        lines = content.readlines()
        print "lines=", len(lines)
        new_lines = []
        for line in lines:
            line = line.strip('\n\t')
            new_lines.append(line)
            print line
        self.lines = new_lines
        self.tokens = []
        self.temp = ""
        self.status = 0

    def add_item(self):
        print "temp", self.temp
        if self.temp in keywords:
            self.status = 2
        self.tokens.append(Token(self.temp, types[self.status]))
        self.temp = ""
        self.status = 0

    def process(self):
        for l in self.lines:
            print "l=", l
            length = len(l)
            index = 0
            while index < length:
                c = l[index]
                if c.isspace():     # 空格
                    index += 1
                    continue
                elif c.isalpha():  # 变量名 关键字
                    self.temp = c
                    self.status = 1
                    index += 1
                    while l[index].isalnum() or l[index] == '_':
                        self.temp += l[index]
                        index += 1
                    self.add_item()
                    continue
                elif c.isdigit():  # 数字 整型 浮点型
                    self.temp = c
                    self.status = 3
                    index += 1
                    while l[index] in numbers2:
                        self.temp += l[index]
                        index += 1
                    self.add_item()
                    continue
                elif c in lbreak_char:
                    self.tokens.append(Token(c, "lbreak"))
                elif c in rbreak_char:
                    self.tokens.append(Token(c, "rbreak"))
                elif c in comma:    # 标点
                    self.tokens.append(Token(c, "comma"))
                elif c in semicolon:    # 标点
                    self.tokens.append(Token(c, "semicolon"))
                elif c in operator:     # 操作符
                    if c == equal:
                        self.tokens.append(Token(c, "equal"))
                    else:
                        self.tokens.append(Token(c, "operator"))
                index += 1

    def display(self):
        for token in self.tokens:
            print token


class ASTNode(object):
    def __init__(self, value=None, _type=None, father=None):
        self.value = value
        self.type = _type
        self.children = []
        # self.father = father


class AST(object):
    def __init__(self):
        # 树的根节点
        self.root = ASTNode()
        # 现在遍历到的节点
        self.current = self.root

    def add_child(self, child, father=None):
        if father is None:
            father = self.current
        father.children.append(child)


class Parser(object):
    p = 0
    def __init__(self, tokens):
        self.tokens = tokens
        self.tree = AST()
        self.lookahead = tokens[:5] #  开辟大小为5的缓冲区
        self.index = 0

    def process(self):
        length = len(self.tokens)
        while self.index < length:
            if self._assignment:
                pass

    def _assignment(self):
        marker = self.index
        flag = True
        try:
            self._id()
            self.match(typess.EQUAL)
            self._expr()
            self.match(typess.SEMICOLON)
        except ValueError:
            flag = False
        finally:
            return flag

    def match(self, _type):

        if self.lookahead[self.p].type == _type:
            self.index += 1
            self.lookahead.append(self.tokens[self.index])
        else:
            raise ValueError

    def _id(self):
        self.match('char')

    def _expr(self):
        if self._num():
            pass
        elif self.

    def _num(self):
        self.match(typess.NUMBERS)


if __name__ == '__main__':
    # path = "D:/Desktop/LIP/complier/test.c"
    path = "D:/Desktop/LIP/complier/assign.c"
    lexer = Lexer(path)
    lexer.process()
    lexer.display()

    parser = Parser(lexer.tokens)
    parser.process()
