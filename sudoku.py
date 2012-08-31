#!/usr/bin/env python
#coding=utf8

from copy import deepcopy

stack = []
results = []

def block(s):
    for top,left in [[0,0], [0,3], [0,6], [3,0], [3,3], [3,6], [6,0], [6,3], [6,6]]:
        exists = []
        for x in range(top, top+3):
            for y in range(left, left+3):
                if isinstance(s[x][y], int):
                    if s[x][y] in exists:
                        s[x][y] = -1
                    else:
                        exists.append(s[x][y])
        for x in range(top, top+3):
            for y in range(left, left+3):
                if isinstance(s[x][y], list):
                    for k in exists:
                        if k in s[x][y]:
                            s[x][y].remove(k)
                    if len(s[x][y]) == 1:
                        if not s[x][y][0] in exists:
                            s[x][y] = s[x][y][0]
                            exists.append(s[x][y])
                        else:
                            s[x][y] = []

    return s
            

def row(s):
    for x in range(0, 9):
        exists = []
        for y in range(0, 9):
            if isinstance(s[x][y], int):
                if s[x][y] in exists:
                    s[x][y] = -1
                else:
                    exists.append(s[x][y])
        for y in range(0, 9):
            if isinstance(s[x][y], list):
                for k in exists:
                    if k in s[x][y]:
                        s[x][y].remove(k)
                if len(s[x][y]) == 1:
                    if not s[x][y][0] in exists:
                        s[x][y] = s[x][y][0]
                        exists.append(s[x][y])
                    else:
                        s[x][y] = []
    return s

def column(s):
    for y in range(0,9):
        exists = []
        for x in range(0,9):
            if isinstance(s[x][y], int):
                if s[x][y] in exists:
                    s[x][y] = -1
                else:
                    exists.append(s[x][y])
        for x in range(0,9):
            if isinstance(s[x][y], list):
                for k in exists:
                    if k in s[x][y]:
                        s[x][y].remove(k)
                if len(s[x][y]) == 1:
                    if not s[x][y][0] in exists:
                        s[x][y] = s[x][y][0]
                        exists.append(s[x][y])
                    else:
                        s[x][y] = []

    return s


def caculate(s):
    s = block(s)
    s = column(s)
    s = row(s)
    return s


def count(s):
    result = 0
    for x in range(0, 9):
        for y in range(0, 9):
            if not isinstance(s[x][y], list):
                result += 1
    return result

def get_coordinate(s):
    min = 10 
    result = None
    for x in range(0, 9):
        for y in range(0, 9):
            if isinstance(s[x][y], list) and len(s[x][y]) < min:
                min = len(s[x][y])
                result = (x, y)
    
    return result 

def check(s):
    for x in range(0, 9):
        for y in range(0, 9):
            if isinstance(s[x][y], list) and len(s[x][y]) == 0:
                return False                
            elif isinstance(s[x][y], int) and s[x][y] == -1:
                return False

    return True


def run(s):
    global results, stack
    p = init(s)
    stack.append(p)
    while len(stack)>0:
        q = stack.pop()
        pre = count(q)
        q = caculate(q)
        current = count(q)
        while check(q):
            if current > pre and current < 81:
                q = caculate(q)
                pre = current
                current = count(q)
            elif current == 81:
                results.append(q)
                break
            elif current == pre:
                x,y = get_coordinate(q)
                for item in q[x][y]:
                    temp = deepcopy(q)
                    temp[x][y] = item
                    stack.append(temp)
                break

def print_list(ls):
    for item in ls:
        print item


def init(s):
    p = [[],[],[],[],[],[],[],[],[]]
    for x in range(0, 9):
        for y in range(0, 9):
            if s[x][y] != 0:
                p[x].append(s[x][y]) 
            else:
                p[x].append([1,2,3,4,5,6,7,8,9])
    p = caculate(p)
    return p
                
def test2():
    global results, stack
    results = []
    stack = []
    s = [[8,0,0,0,0,0,0,0,0],
         [0,0,3,6,0,0,0,0,0],
         [0,7,0,0,9,0,2,0,0],
         [0,5,0,0,0,7,0,0,0],
         [0,0,0,0,4,5,7,0,0],
         [0,0,0,1,0,0,0,3,0],
         [0,0,1,0,0,0,0,6,8],
         [0,0,8,5,0,0,0,1,0],
         [0,9,0,0,0,0,4,0,0]]

    run(s)

    if len(results)>0:
        for item in results:
            print_list(item)
            print "\n"
        print len(results)

def profile_test():
    import profile
    profile.run("test2()")

if __name__=="__main__":
    #test2()
    profile_test()
