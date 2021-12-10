def left_child(index: int):
    return index * 2 + 1

def right_child(index: int):
    return index * 2 + 2

def parent(index:int):
    if index == 0:
        raise ValueError("根节点没有父节点")
    return (index-1)//2


def max_heap(arr: list):
    pass
