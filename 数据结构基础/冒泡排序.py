class BubbleSort:
    def sort(self,array:list):
        n = len(array)
        for i in range(n):
            for j in range(n-i):
                if array[i]>array[j]:
                    temp = array[i]
                    array[i] = array[j]
                    array[j] = temp
        return array

if __name__ == '__main__':
    bs = BubbleSort()
    result = bs.sort()