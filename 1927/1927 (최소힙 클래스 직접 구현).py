import sys


class MinHeap(object):
    def __init__(self):    # MinHeap 객체 선언시, 스스로의 기본 구조 선언
        self.queue = [0]

    def insert(self, n):  # 힙큐 최하단에서 부모 노드를 타고 올라가며 진행한다.
        self.queue.append(n)  # 먼저 입력받은 값을 끝 노드에 위치 시킨다.
        index = len(self.queue) - 1  # 인덱스를 끝 노드를 가리키게 만든다
        while 1 < index:  # 가리키는 인덱스가 루트 노드가 아닐경우 부모 노드와 비교한다.
            p_index = int(index/2) # 일반 이진트리에서 자식의 인덱스는 부모의 2x, 2x + 1 이므로, 자식 인덱스를 2로 나눈뒤, 소숫점을 제외하여 부모 인덱스를 정한다.
            if 0 <= p_index and self.queue[index] < self.queue[p_index]:  # 자신과 부모 노드를 비교하여 부모가 자신보다 크면 부모와 값을 바꾼 후 진행.
                self.swap(index, p_index)
                index = p_index
            else:  # 만약 자신이 부모 노드보다 작은 경우, 힙은 정렬되었으므로 삽입 시퀀스를 종료한다.
                break

    def pop(self):
        e_index = len(self.queue) - 1
        if e_index == 0:
            return 0
        self.swap(1, e_index)
        temp = self.queue.pop()
        self.heapify(1)
        return temp

    def heapify(self, index):
        e_index = len(self.queue) - 1
        l_index = index*2
        r_index = index*2 + 1
        m_index = index

        if l_index <= e_index and self.queue[m_index] > self.queue[l_index]:
            m_index = l_index
        if r_index <= e_index and self.queue[m_index] > self.queue[r_index]:
            m_index = r_index

        if m_index != index:
            self.swap(m_index, index)
            self.heapify(m_index)

    def swap(self, index, p_index):
        self.queue[index], self.queue[p_index] = self.queue[p_index], self.queue[index]


N = int(sys.stdin.readline())
comm = {}
heap = MinHeap()
for i in range(N):
    comm[i] = int(sys.stdin.readline())
    if comm[i] == 0:
        print(heap.pop())
    else:
        heap.insert(comm[i])



