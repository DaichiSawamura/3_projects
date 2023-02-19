class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node


n1 = Node(5)
n2 = Node('a')
n1.next = n2

print(n1.data)
print(n2.data)
print(n1)
print(n2.next)

stack = Stack()
stack.push('data1')
stack.push('data2')
stack.push('data3')
print(stack.top.data)
print(stack.top.next_node.data)
print(stack.top.next_node.next_node.data)
print(stack.top.next_node.next_node.next_node)
print(stack.top.next_node.next_node.next_node.data)