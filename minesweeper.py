import sys
import random


def create_grid(grid, arg):
    i = 0
    j = 0
    while i < arg[1]:
        grid.append([])
        while j < arg[1]:
            grid[i].append('0')
            j = j + 1
        j = 0
        i = i + 1


def disp_grid(grid):
    for i in grid:
        print(i)


def mine_grid(grid, arg):
    bomb_numb = int(0.10 * arg[2])
    while bomb_numb > 0:
        a = random.randint(0, arg[0] - 1)
        b = random.randint(0, arg[1] - 1)
        if grid[a][b] != 'B':
            grid[a][b] = 'B'
            bomb_numb -= 1


def fill_grid(grid, arg):
    for i in range(arg[0]):
        for j in range(arg[1]):
            if grid[i][j] == 'B':
                continue
            grid[i][j] = str(bomb_around(grid, arg, i, j))


def bomb_around(grid, arg, i, j):
    bomb_count = 0
    limit_i = i + 2
    limit_j = j + 2
    i -= 1
    j -= 1
    while i < limit_i and i < arg[0]:
        if i < 0:
            i += 1
            continue
        while j < limit_j and j < arg[1]:
            if j < 0:
                j += 1
                continue
            if i == limit_i - 2 and j == limit_j - 2:
                j += 1
                continue
            if grid[i][j] == 'B':
                bomb_count += 1
            j += 1
        i += 1
        j = limit_j - 3
    return bomb_count


def main():
    arg = [int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[1]) * int(sys.argv[2])]
    arg.sort()
    grid = []
    create_grid(grid, arg)
    mine_grid(grid, arg)
    fill_grid(grid, arg)
    disp_grid(grid)


if __name__ == '__main__':
    main()
