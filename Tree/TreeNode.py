from typing import List, Tuple
from graphviz import Digraph

TreeA = "3,9,20,#,#,15,17"


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def strToTree(s: str) -> TreeNode:
    nodes = s.split(',')
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while i < len(nodes):
        node = queue.pop(0)
        if nodes[i] != "#":
            node.left = TreeNode(nodes[i])
            queue.append(node.left)
        i += 1
        if i < len(nodes) and nodes[i] != "#":
            node.right = TreeNode(nodes[i])
            queue.append(node.right)
        i += 1
    return root


def generateEdges(root: TreeNode, result: List) -> None:
    if root is not None:
        if root.left:
            result.append((root.val, root.left.val))
            generateEdges(root.left, result)
        if root.right:
            result.append((root.val, root.right.val))
            generateEdges(root.right, result)


def plotTree(root: TreeNode, path: str = None, name: str = None) -> None:
    dot = Digraph()
    dot.attr(rankdir='TB', size='8,5')
    dot.attr('node', shape='circle', color='lightblue2', style='filled')

    pathSet = None
    if path:
        pathSet = set()
        pathArr = path.split(',')
        for i in range(len(pathArr) - 1):
            pathSet.add((pathArr[i], pathArr[i + 1]))

    edges: List[Tuple[str, str]] = []
    generateEdges(root, edges)

    for src, dst in edges:
        color = 'red' if pathSet and (src, dst) in pathSet else None
        dot.edge(src, dst, color=color)
    dot.render(f'{name}.gv', view=True)


treeA = strToTree(TreeA)
plotTree(treeA, name='TreeA')
