def solve(lines):
    total_sum = 0
    total_scratch = 0
    cards = {i: 1 for i in range(len(lines))}
    for index,line in enumerate(lines):
        game, numbers = line.split(': ') 
        nw,nh = numbers = numbers.split(' | ')
        nw = [(i) for i in nw.split() if i != ""]
        nh = [(i) for i in nh.split() if i != ""]
        
        w = len(set(nw) & set(nh))

        arr = []
        sum_ = 0

        #part1
        for i in range(len(nh)):
            if nh[i] in nw:
                arr.append(nh[i])

        if len(arr) > 0:
            sum_ = 1
            for _ in range(1, len(arr)):
                sum_ = sum_ * 2 
       # part2 
        for i in range(index + 1, min(len(lines), index + w + 1)):
            cards[i] += cards[index]

        total_sum += sum_

    # don't use sum as variable name, it will mess things up
    # and you will end up spending the next 10 minutes looking for bugs
    total_scratch = sum(cards.values())
    return total_sum, total_scratch

with open('input','r') as input_file:
    lines = input_file.readlines()

print(solve(lines))
