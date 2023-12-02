# naive rushed solution - 11m56s to solve part 1 and part 2
max_red = 12
max_green = 13
max_blue = 14

def strip_current_line(line):
    line = line.strip().replace(':',',').replace(';',',').split(',')
    return line

def solve(lines,part):
    total_sum = 0
    total_power = 0
    for line in lines:
        line = strip_current_line(line)

        id = 0
        red = []
        green = []
        blue = []
        should_add = True
        for v in line:
            number = int(''.join(filter(str.isdigit, v)))
            if "Game" in v:
                id = number 
            if "red" in v:
                red.append(number)
                if number > max_red:
                    should_add = False
            if "green" in v:
                green.append(number)
                if number > max_green: 
                    should_add = False
            if "blue" in v:
                blue.append(number)
                if number > max_blue: 
                    should_add = False
        if should_add:
            total_sum += id
        total_power += max(red) * max(green) * max(blue)

    if part == 1:
        return total_sum
    if part == 2:
        return total_power

with open('input','r') as input_file:
    lines = input_file.readlines()
print(solve(lines,1))
print(solve(lines,2))
