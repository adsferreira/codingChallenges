class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    pass


def deserialize(s):
    pass


if __name__ == '__main__':
    node = Node('root', Node('left', Node('left.left')), Node('right'))
