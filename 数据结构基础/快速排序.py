class QuickSort:
    def sort(self,arr:list):
        n = len(arr)
        i = 0
        j = n-1

        for b in range(n):
            base = arr[b]
            while i<j:
                while i<j and arr[j] >= base:
                    j -= 1
                while i<j and arr[i] <= base:
                    i += 1
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
            