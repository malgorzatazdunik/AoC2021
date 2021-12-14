import numpy as np

def test():
    '''
    5483143223
    2745854711
    5264556173
    6141336146
    6357385478
    4167524645
    2176841721
    6882881134
    4846848554
    5283751526
    '''

    test_input = np.array([
        [5,4,8,3,1,4,3,2,2,3],
        [2,7,4,5,8,5,4,7,1,1],
        [5,2,6,4,5,5,6,1,7,3],
        [6,1,4,1,3,3,6,1,4,6],
        [6,3,5,7,3,8,5,4,7,8],
        [4,1,6,7,5,2,4,6,4,5],
        [2,1,7,6,8,4,1,7,2,1],
        [6,8,8,2,8,8,1,1,3,4],
        [4,8,4,6,8,4,8,5,5,4],
        [5,2,8,3,7,5,1,5,2,6]
    ])

    assert puzzle_1(test_input) == 1656


def puzzle_1(input):
    n_of_steps = 100
    n_of_flashes = 0

    for step in range(n_of_steps):
        input += 1
        flashingOctopuses = np.where(input == 9)
        input[flashingOctopuses] = 0
        n_of_flashes += len(listOfFlashingOctopuses)
        listOfFlashingOctopuses = list(zip(flashingOctopuses[0], flashingOctopuses[1]))
        for i,j in listOfFlashingOctopuses:
            input[i+1][j] += 1
            input[i+1][j+1] += 1
            input[i+1][j-1] += 1
            input[i][j+1] += 1
            input[i][j-1] += 1
            input[i-1][j] += 1
            input[i-1][j-1] += 1
            input[i-1][j+1] += 1



if __name__ == "__main__":
    test()
    # file = open("data/day11.txt")
    # file_contents = file.read()
    # contents_split = file_contents.splitlines()
    # input = contents_split
    # print(puzzle_1(input))
