# Q.  링크드 리스트에서 index번째 원소를 반환하시오.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        node = self.head
        count = 0 # index만큼 가야하므로 카운트하기 위한 변수 count 생성
        while count < index:
            node = node.next
            count += 1 # 이동할 때마다 인덱스에 카운트를 1더해준다.
        return node

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.get_node(0) # -> 5를 들고 있는 노드를 반환해야 합니다!

print(linked_list.get_node(1).data)