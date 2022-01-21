def bubble_sort(array:list):
    """
    要求原地排序
    """
    if array == None or len(array) <= 1:
        return array
    
    for round in range(len(array)):
        compare_times = len(array)-1 - round
        for i in range(0,compare_times): # 控制比较的次数
            if array[i] > array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
    return array
        
        

if __name__ == "__main__":
    array = [6,3,1,7,2]
    print(bubble_sort(array))