import numpy as np
def prepare_data(contents_split):
    coords = []
    instructions = []
    for line in contents_split:
        if 'fold' in line:
            instructions.append(line.split(' ')[-1])
        elif len(line) > 0:
            x = [int(i) for i in line.split(',')]
            coords.append((x[0], x[1]))

    x = None
    y = None
    for line in instructions:
        a = ''.join(line.split(' ')[-1]).split('=')
        if a[0] == 'x':
            if not x:
                x = int(a[1])
        if a[0] == 'y':
            if not y:
                y = int(a[1])
        if x and y:
            break
    max_x = (2*x)+1
    max_y = (2*y)+1
    dots = np.zeros((max_y, max_x))
    for coord in coords:
        dots[coord[1], coord[0]] = 1
    return dots, instructions

def test():
    file = open("data/day13_test.txt")
    file_contents = file.read()
    contents_split = file_contents.splitlines()
    dots, instructions = prepare_data(contents_split)
    print(dots)
    print(instructions)
    assert puzzle_1(dots, instructions) == 17

def puzzle_1(dots, instructions):
    rounds=[]
    for i in instructions:
        x = 0
        y = 0
        if i.split('=')[0] == 'x':
            x = int(i.split('=')[1])
            dots_1 = dots[:, :x]
            dots_2 = dots[:, x+1:]
            dots_2_coords = np.where(dots_2 == 1)
            for a,b in [(i, j) for i,j in zip(dots_2_coords[0],dots_2_coords[1])]:
                dots_1[a, -1-b] = 1
        else:
            y = int(i.split('=')[1])
            dots_1 = dots[:y, :]
            dots_2 = dots[y+1:, :]
            dots_2_coords = np.where(dots_2 == 1)
            for a,b in [(i, j) for i,j in zip(dots_2_coords[0],dots_2_coords[1])]:
                dots_1[-1-a, b] = 1
        dots = dots_1
        rounds.append(np.count_nonzero(dots))
    dots = np.where(dots==1, '@', '.')
    print(dots)
    np.set_printoptions(linewidth=200)
    print(dots.shape)
    return rounds[0]


test()
file = open("data/day13.txt")
file_contents = file.read()
contents_split = file_contents.splitlines()
dots, instructions = prepare_data(contents_split)
print(puzzle_1(dots, instructions))

