# 2019 Kakao Blind Recruitment - 4


def solution(food_times, k):
    n_food = sum(x for x in food_times)

    food_list = []

    # 음식의 수와 반복 횟수 사이의 연관성 생각하기
    # 음식의 수만큼 반복하되, 3으로 나눈 나머지를 구하여 주소값에 매칭
    for i in range(n_food):
        food_list.append(i % 3)

    # print(food_list)
    # food_list = [0, 1, 2, 0, 1, 2]

    # sec: 음식을 섭취하는 시간
    # val + 1: 각 음식의 번호 (1, 2, 3)
    for sec, val in enumerate(food_list):
        idx = sec % 3

        food_times[sec % 3] -= 1

        # 해당 음식을 모두 섭취하여 그 음식의 남은 수가 '-1'이 되는 경우
        if food_times[sec % 3] == -1:
            # continue

            # -- 해당 시점(초)에 먹어야 할 음식을 이미 전부 섭취한 경우,
            # 1) 해당 인덱스(idx)의 값(val) = '-1'에서 '0'으로 변경
            food_times[idx] = 0
            # 2) 다음 음식 섭취 (자리 이동: 인덱스 + 1)
            idx += 1
            food_times[idx % 3] -= 1

        # 해당 시간에 특정 음식을 섭취해야 하는 시간에 네트워크 장애가 발생했을 경우
        # 해당 시간에 특정 음식을 섭취해야 하는 시간과 네트워크 장애가 발생 시간이 일치하는 경우와 같음
        if k == sec:
            result = idx % 3 + 1

        print("{}~{}초 동안 {}번 음식 섭취, 남은 시간: {}".format(sec, sec + 1, idx % 3 + 1, food_times))

    print("{}초에서 네트워크 장애가 발생한 경우, 섭취해야 하는 음식 번호: {}".format(k, result))

    return result


input_k = 5
input_food_times = [3, 1, 2]

print(solution(input_food_times, input_k))
