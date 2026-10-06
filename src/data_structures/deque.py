from typing import Optional


class DequeNode:
    def __init__(self, value):
        self.value = value
        self.prev: Optional["DequeNode"] = None
        self.next: Optional["DequeNode"] = None


class Deque:
    def __init__(self):
        self.front: Optional[DequeNode] = None
        self.back: Optional[DequeNode] = None
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        return f"Deque({self.to_list()})"

    def is_empty(self) -> bool:
        return self._size == 0

    def push_front(self, value) -> None:
        node = DequeNode(value)
        if self.front is None:
            self.front = self.back = node
        else:
            node.next = self.front
            self.front.prev = node
            self.front = node
        self._size += 1

    def push_back(self, value) -> None:
        node = DequeNode(value)
        if self.back is None:
            self.front = self.back = node
        else:
            node.prev = self.back
            self.back.next = node
            self.back = node
        self._size += 1

    def pop_front(self):
        if self.front is None:
            raise IndexError("pop from empty deque")
        value = self.front.value
        self.front = self.front.next
        if self.front is not None:
            self.front.prev = None
        else:
            self.back = None
        self._size -= 1
        return value

    def pop_back(self):
        if self.back is None:
            raise IndexError("pop from empty deque")
        value = self.back.value
        self.back = self.back.prev
        if self.back is not None:
            self.back.next = None
        else:
            self.front = None
        self._size -= 1
        return value

    def peek_front(self):
        return self.front.value if self.front else None

    def peek_back(self):
        return self.back.value if self.back else None

    def to_list(self) -> list:
        result = []
        node = self.front
        while node is not None:
            result.append(node.value)
            node = node.next
        return result
