

class BucketSort:
    def sort(self,array:list):
        n = len(array)
        bucket = [0 for _ in range(max(array)+1)]
        for i in range(n):
            bucket[array[i]] += 1
        result = []
        for i in range(len(bucket)):
            for j in range(bucket[i]):
                result.append(i)
        return result

if __name__ == '__main__':
    bs = BucketSort()
    result = bs.sort([3,1,2,5])
    print(result)