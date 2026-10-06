class Array:
    def __init__(self, capacity: int = 4):
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        self._capacity = capacity
        self._size = 0
        self._data = [None] * capacity

    def __len__(self) -> int:
        return self._size

    def __getitem__(self, index: int):
        self._check_index(index)
        return self._data[index]

    def __setitem__(self, index: int, value):
        self._check_index(index)
        self._data[index] = value

    def __repr__(self) -> str:
        items = ", ".join(repr(self._data[i]) for i in range(self._size))
        return f"Array([{items}])"

    def _check_index(self, index: int) -> None:
        if not 0 <= index < self._size:
            raise IndexError(f"Index {index} out of range [0, {self._size})")

    def _resize(self, new_capacity: int) -> None:
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity

    def push(self, value) -> None:
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        self._data[self._size] = value
        self._size += 1

    def pop(self):
        if self._size == 0:
            raise IndexError("pop from empty array")
        value = self._data[self._size - 1]
        self._data[self._size - 1] = None
        self._size -= 1
        return value

    def insert(self, index: int, value) -> None:
        if not 0 <= index <= self._size:
            raise IndexError(f"Index {index} out of range")
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        for i in range(self._size, index, -1):
            self._data[i] = self._data[i - 1]
        self._data[index] = value
        self._size += 1

    def remove(self, index: int):
        self._check_index(index)
        value = self._data[index]
        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]
        self._data[self._size - 1] = None
        self._size -= 1
        return value

    def find(self, value) -> int:
        for i in range(self._size):
            if self._data[i] == value:
                return i
        return -1
