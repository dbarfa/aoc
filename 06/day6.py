# bad code alert, speedrunned in 9 minutes
# just know your algebra. i just solved the equation through iteration sort of
# part 2 is bruteforced, join the elements of array(n) into a string(1) in arrau and use same algo
 
with open("input","r") as input_file:
    lines = input_file.readlines()

def solution(lines,part):
    time = lines[0].strip().split(':')[1].strip().split()
    distance = lines[1].strip().split(':')[1].strip().split()

    if part == 2:
        time = [''.join(time)]
        distance = [''.join(distance)]

    # let's go
    r = 1
    for i in range(len(time)):
        rr = 0
        for j in range(int(time[i])+1):
            jj = j*(int(time[i])-j)
            if jj > int(distance[i]):
                rr += 1
        r *=rr
    return r

print(solution(lines,2))
