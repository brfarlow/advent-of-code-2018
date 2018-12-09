from collections import defaultdict, deque


def part_1(players, final_point):
    all_players = defaultdict(int)
    marbles = deque([0])
    for player in range(players):
        all_players[player + 1] = 0

    current_player = 0
    current_marble = 0

    for marble in range(1, final_point + 1):
        if marble % 23 == 0:
            all_players[current_player] += marble
            target = (current_marble - 7) % len(marbles)
            marbles.rotate(-target)
            all_players[current_player] += marbles.popleft()
            marbles.rotate(target - 1 + 7)
        else:
            marbles.append(marble)
            marbles.rotate(-1)

        current_marble = len(marbles) - 2
        current_player = (current_player + 1) % players

    return sorted(all_players.values())[-1]


with open('input.txt', 'r') as f:
    input = f.read().split(' ')
    players, final_point = int(input[0]), int(input[6])
    print(part_1(players, final_point))
    print(part_1(players, final_point * 100))
