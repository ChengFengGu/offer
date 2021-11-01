from queue import Queue

class QueuseTest:
    def decrypt(self,arr:list):
        queue = Queue()
        n = len(arr)
        for i in range(n):
            queue.put(arr[i])
        result = Queue()
        while len(queue)>0:
            if len(queue)
            