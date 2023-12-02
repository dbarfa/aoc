
def part1(lines):
    sum = 0
    for line in lines:
        line = ''.join(filter(str.isdigit, line))
        sum = sum + int(line[0] + line[-1])
    return(sum)

def part2(lines):
    wordToNumber = {
        'one': 'one1one',
        'two': 'two2two',
        'three': 'three3three',
        'four': 'four4four',
        'five': 'five5five',
        'six': 'six6six',
        'seven': 'seven7seven',
        'eight': 'eight8eight',
        'nine': 'nine9nine'
    }

    total_sum = 0
    for line in lines:
        line = line.lower()
        for w,d in wordToNumber.items():
            line = line.replace(w, d)
        digits = ''.join(filter(str.isdigit, line))
        total_sum += int(digits[0] + digits[-1])
    return total_sum

with open('input', 'r') as input_file:
    lines = input_file.readlines()

print(part1(lines))
print(part2(lines))
