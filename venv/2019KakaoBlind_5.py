# # 2019 Kakao Blind Recruitment - 2


# def solution(nodeinfo):
#     answer = [[]]
#     return answer


class Node:

    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)  # return as a string


class Tree:

    def __init__(self):  # constructor of class
        self.root = None

    def create(self, d):  # create binary search tree nodes
        if self.root == None:
            self.root = Node(d)

        else:
            current = self.root

            while 1:
                if d < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(d)
                elif d > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(d)
                else:
                    break

    def preorder(self, node):

        if node:
            # print(node.data, end=' ')
            preorder_list.append(node.data)

            if len(preorder_list) == len(nodeInfo):
                print("Preorder\n", preorder_list)
                # result.append(preorder_list)

                for i in range(len(preorder_list)):
                    for j in range(len(x_n)):
                        if preorder_list[i] == x_n[j][0]:
                            preorder_n.append(x_n[j][1])

                print("Preorder\n", preorder_n)
                print()
                result.append(preorder_n)

            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):

        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            # print(node.data, end=' ')
            postorder_list.append(node.data)

            if len(postorder_list) == len(nodeInfo):
                print("Postorder\n", postorder_list)
                # result.append(postorder_list)

                for i in range(len(postorder_list)):
                    for j in range(len(x_n)):
                        if postorder_list[i] == x_n[j][0]:
                            postorder_n.append(x_n[j][1])

                print("Postorder\n", postorder_n)
                print()
                result.append(postorder_n)

    def inorder(self, node):

        if node:
            self.inorder(node.left)
            print(node.data, end=' ')
            self.inorder(node.right)


result = []

preorder_list = []
postorder_list = []
inorder_list = []

preorder_n = []
postorder_n = []
inorder_n = []

nodeInfo = [
    [5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]
]

nodeNum = [i + 1 for i in range(len(nodeInfo))]

sorted_node = sorted(list(zip(nodeInfo, nodeNum)), key=lambda x: x[0][1], reverse=True)
print(sorted_node, "\n")

sorted_node_x = [sorted_node[i][0][0] for i in range(len(sorted_node))]
sorted_node_n = [sorted_node[i][1] for i in range(len(sorted_node))]
print(sorted_node_x)
print(sorted_node_n)
print()

# x_n = dict(zip(sorted_node_x, sorted_node_n))
x_n = tuple(zip(sorted_node_x, sorted_node_n))
print(x_n)
print()

# print([x for x, v in x_n.items()])

# for i in range(len(x_n)):
#     print(x_n[i])

tree = Tree()

for x in sorted_node:
    tree.create(x[0][0])

print("root\n", tree.root)
print()

tree.preorder(tree.root)
tree.postorder(tree.root)
# tree.inorder(tree.root)

print("result\n", result)
