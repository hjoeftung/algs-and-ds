# python3
from collections import deque
from typing import Union, Optional, List, Any


class TreeNode:
    def __init__(self, value: int, parent: int, children: list):
        self.value = value
        self.parent = parent
        self.children = children

    def __repr__(self):
        return f"TreeNode(value={self.value}, parent={self.parent})"

    def add_child(self, node):
        self.children.append(node)
        return self


def convert_to_nodes(parents: List[int]):
    nodes = []
    for index, parent in enumerate(parents):
        nodes.append(TreeNode(value=index, parent=parent, children=[]))
    del parents
    return nodes


def build_tree(nodes: List[TreeNode]):
    for index, node in enumerate(nodes):
        if node.parent != -1:
            nodes[node.parent] = nodes[node.parent].add_child(node)
        else:
            root = node
    return root


def compute_height(root: TreeNode):
    nodes_to_visit = deque()
    nodes_to_visit.append((1, root))
    max_height = 1

    while nodes_to_visit:
        node_to_visit = nodes_to_visit.popleft()

        if node_to_visit[1].children:
            current_height = node_to_visit[0] + 1
            for child in node_to_visit[1].children:
                nodes_to_visit.appendleft((current_height, child))

            if current_height > max_height:
                max_height = current_height
    return max_height


def main(parents):
    nodes = convert_to_nodes(parents)
    root = build_tree(nodes)
    max_height = compute_height(root)
    return max_height


if __name__ == '__main__':
    _ = input()
    parents = list(map(int, input().split()))
    print(main(parents))
