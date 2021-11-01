class QuickSort:
    def sort(self,arr:list):
        n = len(arr)
        i = 0
        j = n-1

        def quick_sort(array:list,left:int,right:int):
            base = array[left]
            while left < right:
                while array[right] >= base:
                    right -= 1
                while array[left] <= base:
                    left += 1
                temp = array[left]
                array[left] = array[right]
                array[right] = temp
            
            arr[left] = base
            
            return array

        