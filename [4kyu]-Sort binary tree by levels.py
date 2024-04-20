class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n


def tree_by_levels(node):
    levels = {}

    def search(current_node, index):
        if not current_node:
            return None
        if index in levels.keys():
            levels[index].append(current_node.value)
        else:
            levels[index] = [current_node.value]
        for child in [current_node.left, current_node.right]:
            search(child, index + 1)
        return None

    search(node, 0)
    result = []
    for level in levels.keys():
        result += levels[level]
    return result


print(tree_by_levels(None), [])
print(tree_by_levels(Node(Node(None, Node(None, None, 4), 2), Node(
    Node(None, None, 5), Node(None, None, 6), 3), 1)), [1, 2, 3, 4, 5, 6])
