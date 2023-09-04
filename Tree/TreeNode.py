class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


"""
      3
    9   20
       15 17
"""


def stringToTree(s: str) -> TreeNode:
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


root = stringToTree("3,9,20,#,#,15,7")
