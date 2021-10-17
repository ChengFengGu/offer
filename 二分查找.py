# 要添加一个新单元，输入 '# %%'
# 要添加一个新的标记单元，输入 '# %% [markdown]'
# %%
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 如果目标值存在返回下标，否则返回 -1
# @param nums int整型一维数组
# @param target int整型
# @return int整型
#


# class Solution:
#     def binary_search(self, nums, left, right, x):
#         if right >= 1:
#             mid = int(1 + (right - 1) / 2)

#             if nums[mid] == x:
#                 return mid
#             elif nums[mid] < x:
#                 return self.binary_search(nums, left, mid - 1, x)
#             elif nums[mid] > x:
#                 return self.binary_search(nums, mid + 1, right, x)

#     def search(self, nums, target):
#         # write code here
#         left = 0
#         right = len(nums) - 1
#         index = self.binary_search(nums, left, right, target)

#         if index == None:
#             return -1

#         if index > 0:
#             while nums[index] == nums[index - 1]:
#                 index -= 1
#         return index


class Solution:
    def search(self, nums, target: int):
        visited = [0 for i in range(len(nums))]

        start = 0
        end = len(nums) - 1
        mid = (start + end) // 2
        if mid < 0:
                mid = 0
        while nums[mid] != target:
            visited[mid] = 1
            if target < nums[mid]:
                start = start
                end = mid - 1
                mid = (start + end) // 2
                if mid < 0:
                    mid = 0
                if visited[mid] == 1:
                    return -1

            if target > nums[mid]:
                start = mid + 1
                end = end
                mid = (start + end) // 2
                if mid > len(nums) - 1:
                    mid = len(nums) - 1
                if visited[mid] == 1:
                    return -1

        while nums[mid] == nums[mid - 1]:
            mid -= 1
        return mid


# %%
if __name__ == "__main__":
    sol = Solution()
    print(sol.search([1, 2, 2, 3, 4], 2))
