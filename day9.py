import pandas as pd
import numpy as np

def prepare(contents_split):
    input = []
    input.append((len(contents_split[0])+2)*[9])
    for line in contents_split:
        row = [9]
        row.extend([int(digit) for digit in line])
        row.append(9)
        input.append(row)
    input.append((len(contents_split[0])+2)*[9])
    print(np.array(input))
    return input

def test():
    file = open("data/day9_test.txt")
    file_contents = file.read()
    contents_split = file_contents.splitlines()
    input = prepare(contents_split)
    assert puzzle_1_2(input) == (15, 1134)


def puzzle_1_2(_input):
    low_points = []
    sizes = []
    for i in range(1, len(_input) - 1):
        for j in range(1, len(_input[i]) - 1):
            point = _input[i][j]
            if point < _input[i][j+1] and point < _input[i+1][j]\
                    and point < _input[i-1][j] and point < _input[i][j-1]:
                low_points.append(point)
                numbers_in_basin = []
                size = len(size_of_basin(_input,i,j, numbers_in_basin))
                sizes.append(size)

    sum = 0
    for p in low_points:
        sum += 1 + p

    print(sum)
    sizes.sort()
    product = 1
    for s in sizes[-3:]:
        product *= s
    print(product)
    return sum, product


def size_of_basin(_input, i, j, numbers_in_basin):
    if (i,j) not in numbers_in_basin:
        numbers_in_basin.append((i, j))
        digits_in_row = []
        digits_in_row.append((i, j))
        x = 1
        t = _input[i][j - x]
        # left
        while t != 9:
            numbers_in_basin.append((i, j-x))
            digits_in_row.append((i, j-x))
            x += 1
            t = _input[i][j - x]
        # right
        z = 1
        t = _input[i][j + z]
        while t != 9:
            numbers_in_basin.append((i, j+z))
            digits_in_row.append((i, j+z))
            z += 1
            t = _input[i][j + z]

        for i,j in digits_in_row:
            if _input[i+1][j] != 9:
                #down
                size_of_basin(_input, i+1,j, numbers_in_basin)

        for i, j in digits_in_row:
            if _input[i-1][j] != 9:
                #up
                size_of_basin(_input, i-1,j, numbers_in_basin)

    return numbers_in_basin

if __name__ == "__main__":
    test()
    file = open("data/day9.txt")
    file_contents = file.read()
    contents_split = file_contents.splitlines()
    input = prepare(contents_split)
    puzzle_1_2(input)

