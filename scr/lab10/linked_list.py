from typing import Any, Iterator


class Node:

    def __init__(self, value: Any, next: "Node | None" = None) -> None:
        self.value: Any = value
        self.next: Node | None = next


class SinglyLinkedList:

    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None
        self._size: int = 0

    def append(self, value: Any) -> None:
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            assert self.tail is not None
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def prepend(self, value: Any) -> None:
        new_node = Node(value, self.head)
        self.head = new_node
        if self._size == 0:
            self.tail = new_node
        self._size += 1

    def insert(self, idx: int, value: Any) -> None:
        if idx < 0 or idx > self._size:
            raise IndexError("Index out of range")

        if idx == 0:
            self.prepend(value)
            return

        if idx == self._size:
            self.append(value)
            return

        current = self.head
        for _ in range(idx - 1):
            assert current is not None
            current = current.next

        new_node = Node(value, current.next)
        current.next = new_node
        self._size += 1

    def remove_at(self, idx: int) -> None:
        if idx < 0 or idx >= self._size:
            raise IndexError("Index out of range")

        if idx == 0:
            assert self.head is not None
            self.head = self.head.next
            if self._size == 1:
                self.tail = None
            self._size -= 1
            return

        current = self.head
        for _ in range(idx - 1):
            assert current is not None
            current = current.next

        assert current.next is not None
        if current.next == self.tail:
            self.tail = current

        current.next = current.next.next
        self._size -= 1

    def __iter__(self) -> Iterator[Any]:
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        values = ", ".join(str(v) for v in self)
        return f"SinglyLinkedList([{values}])"

    def pretty(self) -> str:
        if not self.head:
            return "None"
        parts = []
        current = self.head
        while current:
            parts.append(f"[{current.value}]")
            current = current.next
        parts.append("None")
        return " -> ".join(parts)
