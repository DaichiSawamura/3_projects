class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data, self.top)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        remove = self.top
        self.top = self.top.next_node
        return remove.data


stack = Stack()
stack.push('data1')
stack.push('data2')
data = stack.pop()
print(stack.top.data)
print(data)