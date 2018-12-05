alphabet = 'abcdefghijklmnopqrstuvwxyz'


def destroy_polymer(line):
    current_length = len(line)
    previous_length = current_length + 1
    while current_length != previous_length:
        previous_length = current_length
        for char in alphabet:
            line = line.replace(char + char.upper(), "").replace(char.upper() + char, "")
            current_length = len(line)

    return line


def part_1(line):
    line = destroy_polymer(line)
    return len(line)


def part_2(line):
    line = destroy_polymer(line)
    final_length = len(line)
    for char in alphabet:
        copy = line.replace(char, '').replace(char.upper(), '')
        copy = destroy_polymer(copy)

        if len(copy) < final_length:
            final_length = len(copy)

    return final_length


with open('input.txt', 'r') as f:
    line = f.readlines()[0]
    print(part_1(line))
    print(part_2(line))
