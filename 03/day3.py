from collections import defaultdict
import math

def isSign(character):
    return character != '.' and not str(character).isdigit()

def isStar(character):
    return character == '*'

def checkit(m,pre,curr,next,flagged):
    if flagged == True:
        return True
    flagged = False
    if m - 1 >= 0:
        if isSign(pre[m-1]) or isSign(curr[m-1]) or isSign(next[m-1]):                    
            flagged =  True    
    if isSign(pre[m]) or isSign(curr[m]) or isSign(next[m]):
        flagged = True
    if m + 1 < len(curr):
        if isSign(pre[m+1]) or isSign(curr[m+1]) or isSign(next[m+1]):
            flagged = True
    return flagged

def is2tar(lines, n, m):
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue
            adj_n, adj_m = n + i, m + j
            if adj_n < 0 or adj_m < 0 or adj_n >= len(lines) or adj_m >= len(lines[adj_n]):
                continue
            if isStar(lines[adj_n][adj_m]):
                # print(lines[adj_n][adj_m] + " at position " + str(adj_n) + ", " + str(adj_m))
                return (adj_m, adj_n)
    return 'hello'
def solve(lines):
    total_sum = 0
    num = [] 
    gears = defaultdict(list)
    for n in range(len(lines)):
        lines[n] = lines[n].strip()
        digit = ''
        flagged = False
        stars = set()
        for m in range(len(lines[n])):
            pre = lines[n-1].strip() if n > 0 else lines[n].strip()
            curr = lines[n].strip()
            stars = set()
            next = lines[n+1].strip() if n < len(lines) - 1 else lines[n].strip()
            if curr[m].isdigit():
                digit+=curr[m]
                stars.add(is2tar(lines,n,m)) 
                flagged = checkit(m,pre,curr,next,flagged)
            if m == len(curr) - 1 or not curr[m + 1].isdigit():
                if digit:
                    if flagged:
                        num.append(int(digit))
                        for g in stars:
                            gears[g].append(int(digit))
                digit = ''
                flagged = False
        gears.pop('hello',None)
        print(gears)
    print("Part 2:", sum(math.prod(g) for g in gears.values() if len(g) == 2))
    total_sum = sum(num)
    return total_sum

with open('input') as input_file:
    lines = input_file.readlines()

print(solve(lines))
