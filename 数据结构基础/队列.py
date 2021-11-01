from queue import Queue


class 


class QueuseTest:
    def decrypt(self, arr: list):
        queue = Queue()
        n = len(arr)
        for i in range(n):
            queue.put(arr[i])
        result = []
        while queue.qsize() > 0:
            if queue.qsize() > 1:
                result.append(queue.get())
                queue.put(queue.get())
            elif queue.qsize() == 1:
                result.append(queue.get())
        return result


if __name__ == "__main__":
    qt = QueuseTest()
    result = qt.decrypt(["6", "3", "1", "7", "5", "8", "9", "2", "4"])
    print(result)
