

def create_grid(serial_number):
    grid = [[0 for _ in range(301)] for _ in range(301)]
    for i in range(1, 301):
        for j in range(1, 301):
            rack_id = i + 10
            power_level = rack_id * j
            power_level += serial_number
            power_level = power_level * rack_id
            power_level = (power_level // 100) % 10
            power_level = power_level - 5

            grid[i][j] = power_level

    # https://en.wikipedia.org/wiki/Summed-area_table
    for x in range(1, 301):
        for y in range(1, 301):
            grid[x][y] = grid[x][y] + grid[x - 1][y] + grid[x][y - 1] - grid[x - 1][y - 1]

    return grid


def part_1(serial_number):
    grid = create_grid(serial_number)

    position = (0, 0)
    for x in range(1, 301 - 3):
        for y in range(1, 301 - 3):
            max_power = grid[x + 3][y + 3] - grid[x][y + 3] - grid[x + 3][y] + grid[x][y]

            position = max(position, (max_power, (x + 1, y + 1)))

    return position[1:]


def part_2(serial_number):
    grid = create_grid(serial_number)

    position = (0, (0, 0))

    for grid_size in range(1, 301):
        for x in range(1, 301 - grid_size):
            for y in range(1, 301 - grid_size):
                max_power = grid[x + grid_size][y + grid_size] - grid[x][y + grid_size] - grid[x + grid_size][y] + grid[x][y]

                position = max(position, (max_power, (x + 1, y + 1), grid_size))

    return position[1:]


print(part_1(4151))
print(part_2(4151))
