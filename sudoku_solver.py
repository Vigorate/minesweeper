import
import random


def generate_grid():
    grid = []
    case = []
    line = []

    for u in range(0, 9):
        for j in range(0, 3):
            for i in range(0, 3):
                if random.randint(0, 1) == 0:
                    line.append(random.randint(1, 9))
                else:
                    line.append(0)
            case.append(line)
            line = []
        grid.append(case)
        case = []
    return grid


def check_horizontal_line(grid, nbr, i):
    grid_start = i


def check_vertical_line(grid, nbr, i):



def check_case(grid, nbr, i):
    for j in range(0, 3):
        for w in range(0, 3):
            if grid[i][j][w] == 0:
                grid[i][j][w] = random.randint(1, 9)
            while grid[i][j][w] == nbr:
                random.randint(1, 9)


def correct_grid(grid):
    for i in range(0, 9):
        for j in range(0, 3):
            for w in range(0, 3):
                if grid[i][j][w] > 0:



def main():
    grid = generate_grid()
    for j in range(0, 9, 3):
        for i in range(0, 3):
            print(grid[j + i][0], grid[j + i][1], grid[j + i][2])
    # print("\n")
    # for j in range(0, 9, 3):
    #     print(grid[j][0], grid[j][1], grid[j][2])
    #     print(grid[j + 1][0], grid[j + 1][1], grid[j + 1][2])
    #     print(grid[j + 2][0], grid[j + 2][1], grid[j + 2][2])
    #     print("\n")


main()
