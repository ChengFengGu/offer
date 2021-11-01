class QuickSort:
    def sort(self,arr:list):
        n = len(arr)
        i = 0
        j = n-1

        base = arr[0]

        while i<j:
            while arr[j] >= base:
                j -= 1
            while arr[i] <= base:
                i += 1