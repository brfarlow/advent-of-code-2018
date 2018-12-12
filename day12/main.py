

def calculate_next_gen(current, patterns):
    start = min(current)
    end = max(current)
    next_gen = set()

    for i in range(start - 3, end + 4):
        current_pattern = ''
        for j in range(-2, 3):
            if i + j in current:
                current_pattern += '#'
            else:
                current_pattern += '.'

        if current_pattern in patterns:
            next_gen.add(i)

    return next_gen


def part_1(lines):
    initial_state = lines[0].split(': ')[1]
    patterns = set()
    for line in lines[2:]:
        if line[-1] == '#':
            patterns.add(line[:5])

    current_gen = set(i for i, c in enumerate(initial_state) if c == '#')

    for i in range(20):
        current_gen = calculate_next_gen(current_gen, patterns)

    return sum(current_gen)


with open('input.txt', 'r') as f:
    lines = [line.rstrip('\n') for line in f]
    print(part_1(lines))
