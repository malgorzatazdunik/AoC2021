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
    for round in range(rounds):
        rules = {}
        for ins in instructions:
            pair = ins.split(' -> ')[0]
            insert = ins.split(' -> ')[1]
            if pair in polymer:
                rules[pair] = insert

        indices = []
        pairs = []
        for pair in rules.keys():
            _indices = find_pattern_indices(pair, polymer)
            indices.extend(_indices)
            pairs.extend([pair for i in _indices])

        for i in range(len(indices)):
            pair = pairs[i]
            polymer = insert_to_polymer(polymer, indices[i], rules[pair])
            for index in range(len(indices)):
                if indices[index] > indices[i]:
                    indices[index] += 1

    _most_common = Counter(polymer).most_common()
    most_common_count = max([x[1] for x in _most_common])
    least_common_count = min([x[1] for x in _most_common])
    ans = most_common_count - least_common_count
    return ans


test()
file = open("data/day14.txt")
file_contents = file.read()
contents_split = file_contents.splitlines()
polymer, instructions = prepare_data(contents_split)
print(puzzle(polymer, instructions, 10))
