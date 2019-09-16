# 2020 Kakao Blind Recruitment - 1

import collections


def solution(s):
    d = collections.defaultdict(int)

    for char in string:
        d[char] += 1
        # print(char, d[char], end=' ')

    comp = ''

    for char in d:

        if d[char] == 1:
            comp += char

        else:
            comp += str(d[char]) + char

    return len(comp)


string = "aabbaccc"
print(solution(string))
