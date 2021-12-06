file = open("data/day6.txt")
file_contents = file.read()

arr = file_contents.split(',')

def buckets(num_buckets=9):
    aMap = {}
    for i in range(0, num_buckets):
        aMap[i] = 0
    return aMap

def number_of_fish(start_arr, num_of_days):
    map = buckets()
    for i in range(len(start_arr)):
        fish = start_arr[i]
        map[fish] += 1

    for i in range(num_of_days):
        num_of_zeros = map[0]
        for k in map.keys():
            if k != 8:
                map[k] = map[k+1]

        map[8] = num_of_zeros
        map[6] += num_of_zeros

    sum_of_fish = 0
    for i in range(9):
        sum_of_fish += map[i]
    return sum_of_fish

def test_number_of_fish():
    start_arr = [3,4,3,1,2]
    num_of_days = 18

    output_arr = number_of_fish(start_arr, num_of_days)
    print(output_arr)
    assert output_arr == 26

test_number_of_fish()
arr = [int(x) for x in arr]
answer = number_of_fish(arr, 256)
print(answer)


