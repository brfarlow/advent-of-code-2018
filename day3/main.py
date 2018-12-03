from collections import defaultdict


def get_xy_range(line):
    claim, _, offset, size = line.split()
    x_start, y_start = offset[:-1].split(',')
    x_size, y_size = size.split('x')

    return claim, int(x_start), int(y_start), int(x_size), int(y_size)


def calculate_overlap(lines):
    overlap = defaultdict(int)
    for _, x_start, y_start, x_size, y_size in lines:
        for i in range(x_size):
            for j in range(y_size):
                overlap[(i + x_start, j + y_start)] += 1

    return overlap


def part_1(lines):
    lines = [get_xy_range(line) for line in lines]
    overlap = calculate_overlap(lines)

    square_inches = 0
    for v in overlap.values():
        if v > 1:
            square_inches += 1

    return square_inches


def part_2(lines):
    lines = [get_xy_range(line) for line in lines]
    overlap = calculate_overlap(lines)
    for claim, x_start, y_start, x_size, y_size in lines:
        valid = True
        for i in range(x_size):
            for j in range(y_size):
                if overlap[(i + x_start, j + y_start)] != 1:
                    valid = False
                    break
            if not valid:
                break

        if valid:
            return claim


with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines = [line.rstrip('\n') for line in lines]
    print(part_1(lines))
    print(part_2(lines))
