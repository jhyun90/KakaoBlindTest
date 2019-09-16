# 2019 Kakao Blind Recruitment - 5

nodeInfo = [
    [5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]
]

node_num = []

for i in range(len(nodeInfo)):
    node_num.append(i + 1)

print(node_num, '\n')

x_list = [nodeInfo[i][0] for i in range(len(nodeInfo))]
y_list = [nodeInfo[i][1] for i in range(len(nodeInfo))]

'''
x_list_set = sorted(set([(nodeInfo[i][0]) for i in range(len(nodeInfo))]), reverse=True)
y_list_set = sorted(set([nodeInfo[i][1] for i in range(len(nodeInfo))]), reverse=True)
'''
x_list_set = tuple(sorted(set(x_list), reverse=True))
y_list_set = tuple(sorted(set(y_list), reverse=True))

print(sorted(x_list, reverse=True), '\n', sorted(y_list, reverse=True))
print(x_list_set, '\n', y_list_set)

# 각 노드의 좌표 y 값을 만족하는 좌표의 개수만큼 반복
'''
for y in y_list_set:
    print(y_list.count(y))
'''
y_count = list(map(lambda y: y_list.count(y), y_list_set))
print(y_count)

'''
node_dict = dict(zip(x_list, y_list))
print(node_dict)
sorted_node = sorted(node_dict.items(), key=lambda x: x[1], reverse=True)
print(sorted_node)
'''
sorted_node = sorted(nodeInfo, key=lambda x: x[1], reverse=True)
print(sorted_node)

node_arr = [sorted_node[i][0] for i in range(len(sorted_node))]

for i in range(len(sorted_node)):
    print(sorted_node[i][0])

'''
# 각 노드의 좌표를 노드 번호와 연결
# node_match = [[node[i], node_num[i]] for i in range(len(sorted_node))]
# print(node_match)
'''