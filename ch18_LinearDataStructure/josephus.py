# Define node
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
class LinkedList():
    def __init__(self, data):
        self.head = Node(data)
    
    def append(self, data):
        now = self.head
        while now.next is not None:
            now = now.next  # 이동
        now.next = Node(data)

    def print_all(self):
        now = self.head
        while now is not None:
            print(now.data)
            now = now.next

    def get_node(self, idx):
        count = 0
        node = self.head
        while count < idx:  # 해당 index까지 이동
            count += 1
            node = node.next
        return node
    
    def add(self, idx, value):
        new_node = Node(value)
        if idx == 0:
            new_node.next = self.head   # 새로운 node의 next 지정
            self.head = new_node        # head 포인터 변경
        node = self.get_node(idx-1)     # 삽입 바로 전 idx까지 접근
        next_node = node.next           # 삽입할 자리 뒷부분 노드 저장
        node.next = new_node            # 삽입 노드와 앞부분 연결
        new_node.next = next_node       # 삽입 노드와 뒷부분 연결
    
    def delete(self, idx):
        if idx == 0:
            self.head = self.head.next  # head 포인터를 다음 노드로 변경
            return
        node = self.get_node(idx - 1)   # 삭제 바로 전 idx 접근
        node.next = node.next.next

#############################################################################################
#############################################################################################

def josephus(n: int, k: int):

    survivors = []
    for i in range(1, n+1):
        survivors.append(i)
    
    kill = 0

    while n > 2:

        if kill >= len(survivors):
            kill %= len(survivors)
        
        survivors.pop(kill)
        n -= 1
        kill += k-1
    
    return survivors
        

N, K = map(int, input().split())
surv = josephus(N, K)
print(surv[0], surv[1])

