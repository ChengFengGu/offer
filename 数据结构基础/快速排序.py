class QuickSort:
    def sort(self, arr: list):
        n = len(arr)
        l = 0
        r = n - 1

        def quick_sort(array: list, left: int, right: int):
            
            if left > right:
                return array
            base = array[left]
            i = left
            j = right
            base = array[left]

            while i < j:
                while i < j and array[j] <= base:
                    j -= 1
                while i < j and array[i] >= base:
                    i += 1
                temp = array[i]
                array[i] = array[j]
                array[j] = temp

            array[left] = array[i]
            array[i] = base

            array = quick_sort(array, left, i - 1)
            array = quick_sort(array, i + 1, right)
            return array

        return quick_sort(arr, l, r)


if __name__ == "__main__":
    qs = QuickSort()
    result = qs.sort([1, 4, 3, 2, 5])
    print(result)

