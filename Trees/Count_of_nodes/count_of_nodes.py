from collections import Counter, deque


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


def count_of_nodes(root, queries, st):

    result = []
    for query in queries:
        queue = deque()
        queue.append(root)
        count = 0
        found = False
        while queue:
            current = queue.popleft()
            if current.value == query[0]:
                queue.clear()
                found = True
            if found:
                if st[current.value-1] == query[1]:
                    count += 1

            for child in current.children:
                queue.append(child)
        result.append(count)
    return result


root_1 = Node(1)
root_1.children.append(Node(2))
root_1.children.append(Node(3))


root_2 = Node(1)
root_2.children.append(Node(2))
root_2.children.append(Node(3))
root_2.children.append(Node(7))

root_2.children[0].children.append(Node(4))
root_2.children[0].children.append(Node(5))
root_2.children[1].children.append(Node(6))


s1 = "aba"
s2 = "abaacab"

querires1 = [(1, "a")]
querires2 = [(1, "a"), (2, "b"), (3, "a")]

# querires2 = [(1, "a"), (2, "b"), (3, "a"),(5,"c"),(7,"b")]


print(count_of_nodes(root_1, querires1, s1))
print(count_of_nodes(root_2, querires2, s2))
print(count_of_nodes(root_2, querires2, s2))
# print(get_count(root_2.children[1], s2, "a"))
