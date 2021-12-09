def get_dist_1(pos_1, pos_2):
    return abs(pos_1-pos_2)

def get_dist_2(pos_1, pos_2):
    d = abs(pos_1-pos_2)
    dist = sum([x for x in range(1,d+1)])
    return dist

def puzzle_1(arr):
    min = 100000000000
    ans = 0
    for i in range(max(arr)):
        sum = 0
        for j in arr:
            sum += get_dist_1(i, j)
        if sum < min:
            min = sum
            ans = i
    return min

def puzzle_2(arr):
    min = 100000000000
    ans = 0
    for i in range(max(arr)):
        sum = 0
        for j in arr:
            sum += get_dist_2(i, j)
        if sum < min:
            min = sum
            ans = i
    print(ans)
    return min


def test_puzzle_1():
    test_positions = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    answer = puzzle_1(test_positions)
    print(answer)

    assert answer == 37

def test_puzzle_2():
    test_positions = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    answer = puzzle_2(test_positions)
    print(answer)

    assert answer == 168

test_puzzle_1()
test_puzzle_2()
file = open("data/day7.txt")
file_contents = file.read()

arr = [int(x) for x in file_contents.split(',')]
print(puzzle_1(arr))
print(puzzle_2(arr))
