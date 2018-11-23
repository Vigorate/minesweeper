import sys
import random


def fill_grid(grid, arg):
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
    print("bomb_numb = ", bomb_numb)
    pars_tab = [0, 0]
    while bomb_numb > 0:
        if random.randint(0, arg[2]) == arg[2]:
            grid[pars_tab[0]][pars_tab[1]] = 'B'
            bomb_numb -= 1

#Easy 10% Bombs
#Medium 20%
#Hard 30%

def main():
    arg = [int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[1]) * int(sys.argv[2])]
    arg.sort()
    print(arg)
    grid = []
    fill_grid(grid, arg)
    mine_grid(grid, arg)
    disp_grid(grid)


if __name__ == '__main__':
    main()
