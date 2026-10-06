from typing import Optional


class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left: Optional["AVLNode"] = None
        self.right: Optional["AVLNode"] = None
        self.height = 0


def _height(node: Optional[AVLNode]) -> int:
    return node.height if node else -1


def _update_height(node: AVLNode) -> None:
    node.height = 1 + max(_height(node.left), _height(node.right))


def _balance_factor(node: AVLNode) -> int:
    return _height(node.left) - _height(node.right)


def _rotate_right(y: AVLNode) -> AVLNode:
    x = y.left
    t2 = x.right
    x.right = y
    y.left = t2
    _update_height(y)
    _update_height(x)
    return x


def _rotate_left(x: AVLNode) -> AVLNode:
    y = x.right
    t2 = y.left
    y.left = x
    x.right = t2
    _update_height(x)
    _update_height(y)
    return y


def _rebalance(node: AVLNode) -> AVLNode:
    _update_height(node)
    bf = _balance_factor(node)

    if bf > 1 and _balance_factor(node.left) >= 0:
        return _rotate_right(node)
    if bf > 1 and _balance_factor(node.left) < 0:
        node.left = _rotate_left(node.left)
        return _rotate_right(node)
    if bf < -1 and _balance_factor(node.right) <= 0:
        return _rotate_left(node)
    if bf < -1 and _balance_factor(node.right) > 0:
        node.right = _rotate_right(node.right)
        return _rotate_left(node)
    return node


class AVLTree:
    def __init__(self):
        self.root: Optional[AVLNode] = None

    def insert(self, value) -> None:
        self.root = self._insert(self.root, value)

    def _insert(self, node: Optional[AVLNode], value) -> AVLNode:
        if node is None:
            return AVLNode(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        else:
            return node
        return _rebalance(node)

    def contains(self, value) -> bool:
        node = self.root
        while node is not None:
            if value == node.value:
                return True
            node = node.left if value < node.value else node.right
        return False

    def inorder(self) -> list:
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node: Optional[AVLNode], result: list) -> None:
        if node is None:
            return
        self._inorder(node.left, result)
        result.append(node.value)
        self._inorder(node.right, result)

    def height(self) -> int:
        return _height(self.root)
