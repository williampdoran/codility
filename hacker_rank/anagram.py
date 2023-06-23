def count_occurances(s):
    counts = {}
    for letter in s:
        counts[letter] = counts.get(letter, 0) + 1
    return counts


def anagram(s):
    n = len(s)
    first = s[:(n//2)]
    last = s[(n//2):]
    counts1 = count_occurances(first)
    counts2 = count_occurances(last)
#    print(f'{counts1} \n{counts2}')
    if counts2 == counts1:
        return 0
    elif len(first) != len(last):
        return -1
    else:
        diff = 0
        for k, v in counts1.items():
             diff += max(0, v - counts2.get(k,0))
        return diff
# Write your code here

from collections import Counter

def anagram1(s):
    if len(s) % 2 != 0:
        return -1

    half_len = len(s) // 2
    s1 = s[:half_len]
    s2 = s[half_len:]

    s1_counts = Counter(s1)
    s2_counts = Counter(s2)

    diff = s1_counts - s2_counts
    print(f'{s1_counts} {s2_counts} {diff}')
    return sum(diff.values())

print(anagram('aaabbb'))
print(anagram('ab'))
print(anagram('abc'))
print(anagram('mnop'))
print(anagram('xyyx'))
print(anagram('xaxbbbxx'))