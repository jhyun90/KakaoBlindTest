# 2019 Kakao Blind Recruitment - 2


# def solution(N, stages):
#     answer = []
#
#     return answer


def solution(N, stages):
    N_list = []
    sum_fails = 0
    failures = []
    result = []

    for i in range(1, N + 1):
        N_list.append(i)

        # print(i, [j for j in stages].count(i), len(stages) - sum_fails, [j for j in stages].count(i) / (len(stages) - sum_fails), end='\n')

        failures.append([j for j in stages].count(i) / (len(stages) - sum_fails))

        sum_fails += [j for j in stages].count(i)

    # print(N_list)
    # print(failures)

    res = dict(zip(N_list, failures))
    print(res)

    sorted_res = sorted(res.items(), key=lambda x: x[1], reverse=True)
    print(sorted_res)

    for elem in sorted_res:
        # print(elem[0], ":", elem[1])
        print(elem[0], end=' ')

    return result


N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
# N = 4
# stages = [4, 4, 4, 4, 4]

solution(N, stages)
