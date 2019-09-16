# 2020 Kakao Blind Recruitment - 4

import re


def solution(words, queries):
    answer = []

    for query in queries:
        l = len(query)

        if not query.startswith('?'):
            cnt1 = 0
            query = query.replace('?', '')
            for word in words:
                if l == len(word) and word.startswith(query):
                    # print(word)
                    cnt1 += 1

            answer.append(cnt1)

        if query.startswith('?'):
            cnt2 = 0
            query = query.replace('?', '')
            for word in words:
                if l == len(word) and word.endswith(query):
                    # print(word)
                    cnt2 += 1

            answer.append(cnt2)

    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(words, queries))
