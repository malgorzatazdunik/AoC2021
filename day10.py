def test():
    file = open("data/day10_test.txt")
    file_contents = file.read()
    contents_split = file_contents.splitlines()
    test_input = contents_split
    ans = puzzle_1_2(test_input)
    assert ans == (26397, 288957)


def puzzle_1_2(input):
    dd = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    dd_2 = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }

    dd_3 = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4
    }

    points = 0
    autocompletion_points = []

    for line in input:
        stack = []
        corrupted = False
        for char in line:
            if char in dd_2.keys():
                stack.append(char)
            else:
                el = dd_2[stack.pop()]
                if char != el:
                    points += dd[char]
                    corrupted = True
                    continue

        score = 0
        if len(stack) > 0 and not corrupted:
            score = 0
            for i in range(len(stack) - 1, -1, -1):
                score *= 5
                score += dd_3[stack[i]]
        if score > 0:
            autocompletion_points.append(score)

    autocompletion_points.sort()
    middle_score = autocompletion_points[int(len(autocompletion_points) / 2)]
    return points, middle_score


if __name__ == "__main__":
    test()
    file = open("data/day10.txt")
    file_contents = file.read()
    contents_split = file_contents.splitlines()
    input = contents_split
    print(puzzle_1_2(input))
