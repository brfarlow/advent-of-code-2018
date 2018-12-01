def part_1(lines):
    return sum(lines)


def part_2(lines):
    freq = 0
    seen = [0]
    while True:
        for i in lines:
            freq += i
            if freq in seen:
                return freq

            seen.append(freq)


with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines = list(map(int, lines))

    print(part_1(lines))
    print(part_2(lines))



