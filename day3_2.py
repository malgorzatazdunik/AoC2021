import pandas as pd
import numpy as np

df = pd.read_csv('data/day3.txt', dtype=str, delimiter = "\t", header=None)

_ll = [[x for x in df.iloc[i][0]] for i in range(df.shape[0])]
_ll = np.array(_ll)

def nums(ll, i, most_common):
    if len(ll) == 1:
        global answer
        answer  = ll[0]
        return

    l = ll[:, i]
    zeroes = sum([1 for x in l if x == '0'])
    ones = sum([1 for x in l if x == '1'])

    if most_common:
        if ones >= zeroes:
            ll = ll[(np.where(ll[:, i] == '1'))]
        else:
            ll = ll[(np.where(ll[:, i] == '0'))]
    else:
        if ones >= zeroes:
            ll = ll[(np.where(ll[:, i] == '0'))]
        else:
            ll = ll[(np.where(ll[:, i] == '1'))]

    nums(ll, i+1, most_common)

def convert_to_decimal(x, num, i):
    if i == 0:
        x += num[len(num)-1]
        global output
        output = x
        return

    x += num[len(num)-i-1]*2**i
    i -= 1
    convert_to_decimal(x, num, i)

nums(_ll, 0, True)
ox = answer
nums(_ll, 0, False)
co2 = answer
convert_to_decimal(0, [int(x) for x in ox], len(ox)-1)
ans_ox = output
convert_to_decimal(0, [int(x) for x in co2], len(co2)-1)
ans_co2 = output
print(ans_ox*ans_co2)
