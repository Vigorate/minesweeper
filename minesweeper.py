import sys


def fill_grid(grid):
    i = 0
    j = 0
    while i < int(sys.argv[1]):
        grid.append([])
        while j < int(sys.argv[2]):
            grid[i].append('0')
            j = j + 1
        i = i + 1


def main():
    print(sys.argv)
    grid = []
    fill_grid(grid)
    print(grid)


if __name__ == '__main__':
    main()
