class BubbleSort:
    def sort(self,array:list):
        n = len(array)
        for i in range(n-1):
            for j in range(n-i):
                if array[j]>array[j+1]:
                    temp = array[j]
                    array[j] = array[j+1]
                    array[j+1] = temp
        return array

if __name__ == '__main__':
    bs = BubbleSort()
    result = bs.sort([1,3,2,1])
    print(result)