from heapq import merge
import itertools

list1 = [2, 5, 3]
list2 = [1, 4, 6]
list3 = [7, 9, 8]

# 合并后顺序调整了，但有点问题
list4 = list(merge(list1, list2, list3))
print(list4)

# 合并后排序
list5 = sorted(itertools.chain(list1, list2, list3))
print(list5)
