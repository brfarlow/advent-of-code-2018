from collections import defaultdict


def get_nodes(lines):
    # split the string into ('A', 'B') tuple
    # and make a set of all nodes
    lines = [line.split() for line in lines]
    lines = [(line[1], line[7]) for line in lines]
    # thanks Azia I'm stealing your method for getting the alphabet
    all_nodes = set(chr(i + ord('A')) for i in range(26))
    needed_before = defaultdict(set)
    for (before, after) in lines:
        needed_before[after].add(before)

    return all_nodes, needed_before


def part_1(lines):
    all_nodes, needed_before = get_nodes(lines)

    tree = []
    while all_nodes:
        # get the first root
        # as we pop from the set the children will eventually become a root node
        root = sorted([x for x in all_nodes if (x not in needed_before) or (len(needed_before[x]) == 0)])[0]
        tree.append(root)
        all_nodes.remove(root)
        for child in needed_before:
            if root in needed_before[child]:
                needed_before[child].remove(root)
    return ''.join(tree)


def part_2(lines):
    all_nodes, needed_before = get_nodes(lines)
    total_time = 0
    # 5 workers given
    workers = {k: None for k in range(5)}
    while all_nodes or any(workers.values()):
        for worker in workers:
            if workers[worker]:
                letter, step = workers[worker]
                # 60 seconds + the letter gives the step time
                if step == ord(letter) - ord('A') + 61:
                    for c in needed_before:
                        if letter in needed_before[c]:
                            needed_before[c].remove(letter)
                    workers[worker] = None
                else:
                    workers[worker] = (letter, step + 1)
            if not workers[worker]:
                if all_nodes:
                    # same as part 1
                    # get the root node and add it to the work time / pop from work
                    root = sorted([x for x in all_nodes if (x not in needed_before) or (len(needed_before[x]) == 0)])
                    if root:
                        letter = root[0]
                        workers[worker] = (letter, 1)
                        all_nodes.remove(letter)
        total_time += 1

    # extra second added because of the loop
    # lovely one off errors
    return total_time - 1


with open('input.txt', 'r') as f:
    lines = f.readlines()
    lines = [line.rstrip('\n') for line in lines]
    print(part_1(lines))
    print(part_2(lines))