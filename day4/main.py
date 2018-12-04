import re
from collections import defaultdict


def get_total_sleep_time(lines):
    lines.sort()
    guards = defaultdict(lambda: defaultdict(int))
    times = defaultdict(int)
    guard_id = None
    asleep = None
    for line in lines:
        timestamp = re.findall(r"\[(.*?)\]", line)[0]
        date, hour_minute = timestamp.split(' ')
        minute = int(hour_minute.split(':')[1])
        if '#' in line:
            guard_id = int(line.split(' ')[3].strip('#'))
            asleep = None
        elif 'asleep' in line:
            asleep = minute
        else:
            for i in range(asleep, minute):
                guards[guard_id][i] += 1
                times[guard_id] += 1

    return guards, times


def part_1(lines):
    guards, times = get_total_sleep_time(lines)
    most_asleep_guard = max(guards.keys(), key=lambda x: sum(guards[x].values()))
    most_asleep_minute = max(guards[most_asleep_guard].keys(), key=lambda x: guards[most_asleep_guard][x])

    return most_asleep_guard * most_asleep_minute


def part_2(lines):
    guards, times = get_total_sleep_time(lines)
    most_asleep_minute = {guard: max(guards[guard].keys(), key=lambda x: guards[guard][x]) for guard in guards.keys()}
    most_asleep_guard = max(guards.keys(), key=lambda x: guards[x][most_asleep_minute[x]])

    return most_asleep_minute[most_asleep_guard] * most_asleep_guard


with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines = [line.rstrip('\n') for line in lines]
    print(part_1(lines))
    print(part_2(lines))
