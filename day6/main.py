from collections import Counter
import re


def manhattan_distance(first, other):
    return abs(first[0] - other[0]) + abs(first[1] - other[1])


def part_1(lines):
    # turn input into x,y coords
    tuples = [tuple(map(int, re.findall('\d+', i))) for i in lines]
    # find min and max x,y
    min_x = min(x[0] for x in tuples)
    max_x = max(x[0] for x in tuples)
    min_y = min(y[1] for y in tuples)
    max_y = max(y[1] for y in tuples)

    max_area = 0
    counter = Counter()
    # loop through the x,y coords
    for i in range(min_x, max_x):
        for j in range(min_y, max_y):
            # get the manhattan distance for the current x,y and current point
            distances = [manhattan_distance((i, j), point) for point in tuples]

            # sort the distances to make sure we're not equidistant from
            # multiple points
            sorted_dists = sorted(distances)
            if sorted_dists[0] != sorted_dists[1]:
                # we're not equidistant so add to the total area surrounding
                # the tuple at the index of the distance
                counter[tuples[distances.index(sorted_dists[0])]] += 1

    for point in tuples:
        # non-infinite if the point is between other points (within min/max bounds)
        if (min_x < point[0] < max_x) and (min_y < point[1] < max_y):
            # max is current max or the highest area from the counter
            max_area = max(max_area, counter[point])

    return max_area


def part_2(lines):
    # turn input into x,y coords
    tuples = [tuple(map(int, re.findall('\d+', i))) for i in lines]
    # find min and max x,y
    min_x = min(x[0] for x in tuples)
    max_x = max(x[0] for x in tuples)
    min_y = min(y[1] for y in tuples)
    max_y = max(y[1] for y in tuples)

    size = 0
    # loop through the x,y coords
    for i in range(min_x, max_x):
        for j in range(min_y, max_y):
            # find the manhattan distance for this point and x,y
            distances = [manhattan_distance((i, j), point) for point in tuples]
            # if less than 10k its within the region size
            if sum(distances) < 10000:
                size += 1

    return size


with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines = [line.rstrip('\n') for line in lines]
    print(part_1(lines))
    print(part_2(lines))