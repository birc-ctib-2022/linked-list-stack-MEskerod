"""Testing our stack implementation."""

from stack import Stack

def test_create_stack():
    stack = Stack()
    assert str(stack) == "[]"

def test_push_to_stack(): 
    stack = Stack()
    stack.push(1)
    assert str(stack) == "[1]"
    stack.push(3) 
    assert str(stack) == "[1, 3]"
    stack.push(5)
    stack.push(1)
    assert str(stack) == "[1, 3, 5, 1]"
    stack.push(-4) 
    assert str(stack) =="[1, 3, 5, 1, -4]"

def test_top_of_stack():
    stack = Stack()
    stack.push(1)
    assert stack.top() == 1
    stack.push(3) 
    assert stack.top() == 3
    stack.push(5)
    stack.push(1)
    assert stack.top() == 1
    stack.push(-4) 
    assert stack.top() == -4

def test_pop_from_stack(): 
    stack = Stack()
    stack.push(1)
    stack.push(3)
    assert stack.pop() == 3 
    assert str(stack) == "[1]"
    stack.push(5)
    stack.push(1)
    stack.push(-4) 
    assert stack.pop() == -4
    assert str(stack) == "[1, 5, 1]"
    assert stack.pop() == 1
    assert str(stack) == "[1, 5]"
    assert stack.pop() == 5
    assert stack.pop() == 1
    assert str(stack) == "[]"

def test_is_stack_empty(): 
    stack = Stack()
    assert stack.is_empty() == True
    stack.push(5)
    assert stack.is_empty() == False
