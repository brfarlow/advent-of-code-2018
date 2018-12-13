

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

    current_gen = set(i for i, j in enumerate(initial_state) if j == '#')

    for i in range(20):
        current_gen = calculate_next_gen(current_gen, patterns)

    return sum(current_gen)


def part_2(lines):
    initial_state = lines[0].split(': ')[1]
    patterns = set()
    for line in lines[2:]:
        if line[-1] == '#':
            patterns.add(line[:5])

    current_gen = set(i for i, j in enumerate(initial_state) if j == '#')

    current_sum = sum(current_gen)
    previous_sum = 0
    for i in range(1000):
        previous_sum = current_sum
        current_gen = calculate_next_gen(current_gen, patterns)
        current_sum = sum(current_gen)

    diff = current_sum - previous_sum
    return (50000000000 - 1000) * diff + current_sum


with open('input.txt', 'r') as f:
    lines = [line.rstrip('\n') for line in f]
    print(part_1(lines))
    print(part_2(lines))
