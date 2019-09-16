# 2019 Kakao Blind Recruitment - 3

'''
[
    ["100","ryan","music","2"],
    ["200","apeach","math","2"],
    ["300","tube","computer","3"],
    ["400","con","computer","4"],
    ["500","muzi","music","3"],
    ["600","apeach","music","2"]
]
'''

'''
후보키의 개수를 return 하도록 함수 정의
1. row 별로 중복 검사
2. row 내에 중복이 없는 경우 -> 후보키 가능, 최소성 & 유일성
3. row 내에 중복이 있는 경우 -> 다른 row와의 결합을 통해 유일성 획득 & 꼭 필요한 row만 넣어서 최소성 확립할 수 있게 하기
'''

input_relation = [
    ["100","ryan","music","2"],
    ["200","apeach","math","2"],
    ["300","tube","computer","3"],
    ["400","con","computer","4"],
    ["500","muzi","music","3"],
    ["600","apeach","music","2"]
]


def solution(relation):
    attr_list = [[relation[j][i] for j in range(len(relation))] for i in range(len(relation[0]))]
    # attr_list = zip(*relation)

    # for row in attr_list:
    #     print(row))

    attr_set = [set([relation[j][i] for j in range(len(relation))]) for i in range(len(relation[0]))]
    # print(attr_list)
    # print(attr_set)
    # print()
    # print([[x for x in row][:] for row in attr_list])

    for i in range(len(attr_list)):
        if len(attr_list[i]) == len(attr_set[i]):
            primaryKey = attr_list[i]

    # print(primaryKey, '\n')

    # a = [tuple([attr_list[1][i], attr_list[2][i]]) for i in range(len(attr_list[0]))]
    # b = [tuple([attr_list[2][i], attr_list[3][i]]) for i in range(len(attr_list[0]))]
    # c = [tuple([attr_list[1][i], attr_list[3][i]]) for i in range(len(attr_list[0]))]
    #
    # print(set(a))
    # print(set(b))
    # print(set(c))
    #
    # if len(set(a)) == len(primaryKey):
    #     compositeKey = a
    # elif len(set(b)) == len(primaryKey):
    #     compositeKey = b
    # else:
    #     compositeKey = c
    #
    # print(compositeKey)

    composite_set = []

    for i in range(1, len(attr_list)):
        for j in range(i + 1, len(attr_list)):
            a = [tuple([attr_list[i][k], attr_list[j][k]]) for k in range(len(attr_list[0]))]
            composite_set.append(set(a))

    # print(composite_set, '\n')

    for row in composite_set:
        # print(row)
        if len(row) == len(primaryKey):
            compositeKey = row

    # print(compositeKey, '\n')

    final = primaryKey, compositeKey
    n_candidateKeys = len(final)
    result = n_candidateKeys
    # print(answer)

    return result


print(solution(input_relation))

# 이중 리스트 안에 각 원소를 추출하여 해당 원소가 그 행 안에 포함되어 있는 경우 true 반환, 아닐 경우 false 반환
