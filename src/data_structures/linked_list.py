from typing import Optional


class Node:
    def __init__(self, value):
        self.value = value
        self.next: Optional["Node"] = None


class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        values = [str(v) for v in self]
        return f"LinkedList([{', '.join(values)}])"

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def is_empty(self) -> bool:
        return self._size == 0

    def push_front(self, value) -> None:
        node = Node(value)
        node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = node
        self._size += 1

    def push_back(self, value) -> None:
        node = Node(value)
        if self.tail is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self._size += 1

    def pop_front(self):
        if self.head is None:
            raise IndexError("pop from empty list")
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self._size -= 1
        return value

    def find(self, value) -> Optional[Node]:
        current = self.head
        while current is not None:
            if current.value == value:
                return current
            current = current.next
        return None

    def remove(self, value) -> bool:
        prev = None
        current = self.head
        while current is not None:
            if current.value == value:
                if prev is None:
                    self.head = current.next
                    if self.head is None:
                        self.tail = None
                else:
                    prev.next = current.next
                    if current is self.tail:
                        self.tail = prev
                self._size -= 1
                return True
            prev = current
            current = current.next
        return False

    def to_list(self) -> list:
        return list(self)
