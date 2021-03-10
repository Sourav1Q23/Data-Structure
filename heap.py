class MinHeap(object):
    
    def __init__(self):
        self.heap= []

    def buildHeap(self, array):
        firstParentIdx = (len(array) - 2) // 2
        for currentIdx in reversed(range(firstParentIdx + 1)):
            self._siftDown(currentIdx, len(array) - 1, array)
        return array

    def _getSize(self):
        return len(self.heap)

    def insert(self,value):
        self.heap.append(value)
        self._siftUp(len(self.heap)-1,self.heap)

    def pop(self):
        if not self._getSize():
            return "Heap Is Empty "
        elif self._getSize()==1:
            return self.heap.pop()
        else:
            self.heap[0],self.heap[-1] = self.heap[-1], self.heap[0]
            val = self.heap.pop()
            self._siftDown(0,len(self.heap)-1, self.heap)
            return val

    def min(self):
        if not self.heap:
            return None
        return self.heap[0]

    def _siftDown(self, currentIdx, endIdx, heap):
        childOneIdx = currentIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
            if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
            if heap[idxToSwap] < heap[currentIdx]:
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                return

    def _siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]