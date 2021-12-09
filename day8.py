def aMap(n):
    map = {}
    for i in range(n):
        map[i] = 0
    return map

def test_puzzle_1():
    file = open("data/day8_test.txt")
    file_contents = file.read()
    contents_split = file_contents.splitlines()

    assert puzzle_1(contents_split) == 26

def test_puzzle_2():
    file = open("data/day8_test.txt")
    file_contents = file.read()
    contents_split = file_contents.splitlines()

    assert puzzle_2(contents_split) == 61229

def puzzle_1(contents_split):
    map = aMap(9)
    for line in contents_split:
        wires = ''.join((''.join(line).split(' | ')[0])).split(' ')
        output_values = ''.join((''.join(line).split(' | ')[1])).split(' ')

        for digit in output_values:
            if len(digit) == 2:
                map[1] += 1
            elif len(digit) == 3:
                map[7] += 1
            elif len(digit) == 4:
                map[4] += 1
            elif len(digit) == 7:
                map[8] += 1

    sum = 0
    for key in map.keys():
        sum += map[key]

    return sum


def puzzle_2(contents_split):
    sum = 0
    map = {}
    for i in range(9):
        map[i] = ''
    for line in contents_split:
        wires = ''.join((''.join(line).split(' | ')[0])).split(' ')
        output_values = ''.join((''.join(line).split(' | ')[1])).split(' ')
        map = aMap(10)
        for digit in wires:
            if len(digit) == 2:
                map[1] = digit
            elif len(digit) == 3:
                map[7] = digit
            elif len(digit) == 4:
                map[4] = digit
            elif len(digit) == 7:
                map[8] = digit
        for digit in wires:
            if len(digit) == 5:
                if set(map[1]) == set(digit).intersection(map[1]):
                    map[3] = digit
                elif set(set(map[8]) - set(digit)) == set(set(map[4]) - set(digit)):
                    map[2] = digit
                else:
                    map[5] = digit

            if len(digit) == 6:
                if set(digit).union(set(map[1])) == set(map[8]):
                    map[6] = digit
                elif set(map[4]) == set(digit).intersection(set(map[4])):
                    map[9] = digit
                else:
                    map[0] = digit

        output = ''
        for o in output_values:
            for key in map.keys():
                if set(map[key]) == set(o):
                    output += str(key)

        sum += int(output)

    return sum

if __name__ == "__main__":
    test_puzzle_1()
    file = open("data/day8.txt")
    file_contents = file.read()
    contents_split = file_contents.splitlines()
    ans = puzzle_1(contents_split)
    print(ans)

    #
    # file = open("data/day8_test.txt")
    # file_contents = file.read()
    # contents_split = file_contents.splitlines()
    ans_2 = puzzle_2(contents_split)
    print(ans_2)