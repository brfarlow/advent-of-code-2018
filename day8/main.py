

def parse_nodes(data):
    # the current node is always the first 2 two numbers passed in
    # that consist of the children and metadata values
    len_children, len_metadata = data[:2]
    # remove the current node from the data
    data = data[2:]
    final = 0

    for _ in range(len_children):
        total, data = parse_nodes(data)
        final += total

    # no more children, the metadata is is the next x value from len_metadata
    final += sum(data[:len_metadata])

    return final, data[len_metadata:]


def parse_nodes_2(data):
    len_children, len_metadata = data[:2]
    data = data[2:]
    values = []
    final = 0

    for _ in range(len_children):
        total, value, data = parse_nodes_2(data)
        final += total
        values.append(value)

    metadata = data[:len_metadata]
    data = data[len_metadata:]
    final += sum(metadata)

    if not len_children:
        return final, sum(metadata), data
    else:
        value = sum(values[x - 1] for x in metadata if 0 < x <= len(values))
        return final, value, data


def part_1(data):
    return parse_nodes(data)


def part_2(data):
    return parse_nodes_2(data)


with open('input.txt', 'r') as f:
    lines = f.read()
    data = [int(x) for x in lines.split()]
    print(part_1(data))
    print(part_2(data))
