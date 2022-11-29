"""A linked list implementation of a stack."""

from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, TypeVar, Optional

T = TypeVar('T')


@dataclass
class Link(Generic[T]):
    """A link in a linked list."""

    head: T
    tail: List[T]


List = Optional[Link[T]]


class Stack(Generic[T]):
    """A stack of elements of (generic) type T."""

    def __init__(self) -> None:
        """Create a new stack of values of type T."""
        self.stack = Link(None, None)

    def __eq__(self, other: object) -> bool:
        return self.stack.tail == other.stack.tail and self.stack.head == other.stack.head
    
    def __repr__(self) -> str:
        if self.is_empty():
            return "[]"
        stack = []
        x = self.stack
        while x: 
            stack.append(x.head)
            x = x.tail
        stack.reverse()
        return "{}".format(stack)
        #return f'Link({self.stack.head}, {self.stack.tail})'
    
    def push(self, x: T) -> None:
        """Push x on the top of this stack."""
        if self.is_empty():
            self.stack = Link(x, self.stack.tail)
        else: 
            self.stack = Link(x, self.stack)

    def top(self) -> T:
        """Return the top of the stack."""
        return self.stack.head

    def pop(self) -> T:
        """Pop the top element off the stack and return it."""
        value = self.stack.head
        if not self.stack.tail:
            self.stack = Link(None, None)
        else:
            self.stack = self.stack.tail
        return value

    def is_empty(self) -> bool:
        """Test if the stack is empty."""
        if not self.stack.head and not self.stack.tail:
            return True
        else: 
            return False

stack = Stack()
stack.push(1)
print(stack)
stack.push(3)
print(stack)