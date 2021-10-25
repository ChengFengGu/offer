class LinearSearch:
    def search(self,data:list,target:int):
        for i in range(len(data)):
            if data[i] == target:
                return i