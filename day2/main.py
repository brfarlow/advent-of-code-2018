def part_1(lines):
    twice = 0
    thrice = 0
    for line in lines:
        seen_twice = False
        seen_thrice = False
        for i in line:
            if line.count(i) == 2 and seen_twice is False:
                twice += 1
                seen_twice = True
            if line.count(i) == 3 and seen_thrice is False:
                thrice += 1
                seen_thrice = True

    return twice * thrice


def part_2(lines):
    for line in lines:
        for item in lines:
            diff = [i for i in range(len(line)) if line[i] != item[i]]
            if len(diff) == 1:
                return line[:diff[0]] + line[diff[0]+1:]


with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines = [line.rstrip('\n') for line in lines]
    print(part_1(lines))
    print(part_2(lines))
