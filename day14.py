import numpy as np
import re
from collections import Counter


def prepare_data(contents_split):
    polymer = ''
    instructions = []
    for line in contents_split:
        if '->' in line:
            instructions.append(line)
        elif len(line) > 0:
            polymer = line
    return polymer, instructions


def test():
    file = open("data/day14_test.txt")
    file_contents = file.read()
    contents_split = file_contents.splitlines()
    polymer, instructions = prepare_data(contents_split)
    assert puzzle(polymer, instructions, 10) == 1588


def insert_to_polymer(polymer, index, insert):
    polymer = polymer[:index+1] + insert + polymer[index+1:]
    return polymer

def find_pattern_indices(pattern, string):
    indices = []
    for letter in range(len(string)-1):
        if string[letter:letter+2] == pattern:
            indices.append(letter)

    return indices

def puzzle(polymer, instructions, rounds):

    pairs_in_polymer = {}
    for i in range(len(polymer)-1):
        if polymer[i:i+2] in pairs_in_polymer.keys():
            pairs_in_polymer[polymer[i:i+2]] += 1
        else:
            pairs_in_polymer[polymer[i:i + 2]] = 1

    counts = {}
    for letter in set(polymer):
        counts[letter] = polymer.count(letter)

    for round in range(rounds):
        pairs_to_add = {}
        pairs_to_delete = {}

        for ins in instructions:
            pair = ins.split(' -> ')[0]
            insert = ins.split(' -> ')[1]
            if pair in pairs_in_polymer.keys():
                new_pair_1 = pair[0] + insert
                new_pair_2 = insert + pair[1]
                if (new_pair_1, new_pair_2) in pairs_to_add.keys():
                    pairs_to_add[(new_pair_1, new_pair_2)] += pairs_in_polymer[pair]
                else:
                    pairs_to_add[(new_pair_1, new_pair_2)] = pairs_in_polymer[pair]

                if pair in pairs_to_delete.keys():
                    pairs_to_delete[pair] += pairs_in_polymer[pair]
                else:
                    pairs_to_delete[pair] = pairs_in_polymer[pair]


        for new_pair, old_pair in zip(pairs_to_add.keys(), pairs_to_delete):
            new_pair_1 = new_pair[0]
            new_pair_2 = new_pair[1]
            insert = new_pair_1[1]
            if new_pair_1 in pairs_in_polymer.keys():
                pairs_in_polymer[new_pair_1] += pairs_to_delete[old_pair]
            else:
                pairs_in_polymer[new_pair_1] = pairs_to_delete[old_pair]

            if new_pair_2 in pairs_in_polymer.keys():
                pairs_in_polymer[new_pair_2] += pairs_to_delete[old_pair]
            else:
                pairs_in_polymer[new_pair_2] = pairs_to_delete[old_pair]

            if insert in counts.keys():
                counts[insert] += pairs_to_delete[old_pair]
            else:
                counts[insert] = pairs_to_delete[old_pair]

            pairs_in_polymer[old_pair] -= pairs_to_delete[old_pair]

    most_common_count = max(counts.values())
    least_common_count = min(counts.values())
    ans = most_common_count - least_common_count
    return ans


test()
file = open("data/day14.txt")
file_contents = file.read()
contents_split = file_contents.splitlines()
polymer, instructions = prepare_data(contents_split)
print(puzzle(polymer, instructions, 40))
