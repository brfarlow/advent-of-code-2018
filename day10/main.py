import re

import matplotlib.pyplot as plt


def part_1(lines):
    positions = []
    for i in range(15000):
            min_x = min(x + i * vx for (x, y, vx, vy) in lines)
            max_x = max(x + i * vx for (x, y, vx, vy) in lines)
            min_y = min(y + i * vy for (x, y, vx, vy) in lines)
            max_y = max(y + i * vy for (x, y, vx, vy) in lines)
            positions.append([min_x, max_x, min_y, max_y])

    closest_point = min(max_x - min_x + max_y - min_y for min_x, max_x, min_y, max_y in positions)

    position = None
    for i, (min_x, max_x, min_y, max_y) in enumerate(positions):
        if closest_point == max_x - min_x + max_y - min_y:
            position = i
            break

    x = [x + position * vx for x, y, vx, vy in lines]
    y = [y + position * vy for x, y, vx, vy in lines]
    plt.gca().invert_yaxis()
    plt.scatter(x, y)
    plt.show()

    return position


with open('input.txt', 'r') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]
    lines = [[int(i) for i in re.findall(r'-?\d+', line)] for line in lines]
    print(part_1(lines))
