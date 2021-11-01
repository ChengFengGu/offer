class QuickSort:
    def sort(self,arr:list):
        n = len(arr)
        i = 0
        j = n-1

        def quick_sort(array:list,left:int,right:int):
            base = array[left]
            if left > right:
                return array

            i = left
            j = right
            base = array[left]

            while i<j:
                while array[j] >= base:
                    j -= 1
                while array[i] <= base:
                    i += 1
                temp = array[i]
                array[i] = array[j]
                array[j] = temp

            array[left] = array[i]
            array[i] = base
            
            array = 

        