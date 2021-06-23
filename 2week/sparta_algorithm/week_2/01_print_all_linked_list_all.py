# node는 데이터와 다음칸을 나타내는 값을 나타내는 포인터가 있어야 한다.
# data, next

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node = Node(3)
first_node = Node(4)
node.next = first_node
print(node.data)

class LinkedList:
    def __init__(self, data):
        self.head =  Node(data)

linked_list = LinkedList(3)

print(linked_list.head.data)