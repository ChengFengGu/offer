"""

堆排序

steps:
---

1. 用无序序列构建一个堆(无序堆),堆顶是最大元素
2. 将堆顶R[0]和无序区的最后一个记录R[n-1]交换,由此得到新的无序区R[0...n-2]和有序区R[n-1],且满足R[0,..n-2].keys ≤ R[n-1].key
3. 由于交换后新的根R[1]可能会违反堆性质,故将当前无序区R[1..n-1]调整为堆,然后重复类似2的操作.
4. 直到无序区只剩一个元素为止.

"""


def heap_sort(arr: list):

    # step1 将数组堆化
    length = len(arr) - 1  # 无序序列
    def swap(i:int,j:int):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def maxHeatify(index: int, len: int):
        li = (index << 1) + 1
        ri = li + 1
        cMax = li
        if li > length:
            return
        if ri <= length and arr[ri] > arr[li]:
            cMax = ri
        if arr[cMax] > arr[index]:
            swap(cMax,index)
            maxHeatify(cMax,len)
    
    begin_index = (length - 1) >> 1
    for i in range(begin_index, -1, -1):
        maxHeatify(i, len)
    
    return arr
if __name__ == "__main__":
    a = [3,5,3,0,8,6,1,5,8,6,2,4,9,4,7,0,1,8,9,7,3,1,2,5,9,7,4,0,2,6]
    result = heap_sort(a)
    print(a)