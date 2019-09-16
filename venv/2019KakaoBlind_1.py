# 2019 Kakao Blind Recruitment - 1

'''
record:
[“Enter uid1234 Muzi”, “Enter uid4567 Prodo”,”Leave uid1234”,”Enter uid1234 Prodo”,”Change uid4567 Ryan”]
result:
[“Prodo님이 들어왔습니다.”, “Ryan님이 들어왔습니다.”, “Prodo님이 나갔습니다.”, “Prodo님이 들어왔습니다.”]
'''

'''
Enter uid1234 Muzi
Enter uid4567 Prodo
Leave uid1234 Muzi
Enter uid1234 Prodo
Change uid4567 Ryan
'''

'''
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234 Muzi", "Enter uid1234 Prodo", "Change uid4567 Ryan"]

for i in range(len(record)):
    print(record[i])

for i in record:
    print(i.split())
'''


def solution(record):
    sub_record = []
    db_users_dict = {}
    result = []

    for message in record:
        sub_record.append(message.split())

    # print(sub_record)

    for i in range(len(sub_record)):
        # print(sub_record[i])
        if sub_record[i][0] == "Enter" or sub_record[i][0] == "Change":
            db_users_dict[sub_record[i][1]] = sub_record[i][2]

    for i in range(len(sub_record)):
        if sub_record[i][0] == "Enter":
            result.append(db_users_dict[sub_record[i][1]] + "님이 들어왔습니다.")
        elif sub_record[i][0] == "Leave":
            result.append(db_users_dict[sub_record[i][1]] + "님이 나갔습니다.")

    return result


input1_record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
input2_record = ["Enter uid1434 Muzi", "Enter uid4567 Prodo", "Leave uid1434", "Enter uid1234 Prodo", "Change uid4567 Ryan", "Enter uid4067 AAA"]

print(solution(input1_record))
print(solution(input2_record))
