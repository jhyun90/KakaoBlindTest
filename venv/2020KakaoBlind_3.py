# 2020 Kakao Blind Recruitment - 3


def solution(key, lock):
    rotation = []

    for i in range(len(key[0])):
        row = []

        for j in reversed(range(len(key))):
            row.append(key[j][i])
            # print(a[j][i], end=' ')

        rotation.append(row)

    # print(rotation)

    for i in range(len(rotation)):
        rotation[i] = [rotation[i].pop(2)] + rotation[i]
        # print(rotation[i])

    # print(rotation)

    cnt = [0, 0, 0]

    for i in range(len(rotation)):
        for j in range(len(rotation[i])):
            if i <= 1 and rotation[i][j] == 1 and rotation[i + 1][j] == 0:
                if cnt[j] >= 1:
                    continue

                rotation[i][j] = 0
                rotation[i + 1][j] = 1
                cnt[j] += 1

    # print(rotation)

    result = ''

    for i in range(len(rotation)):
        for j in range(len(rotation[i])):
            if lock[i][j] == 0 and rotation[i][j] == 1:
                    result = "True"

    return True


key = [
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 1]
]

lock = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]

print(solution(key, lock))
