import numpy as np

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 0
        right = len(nums) - 1
        ans = [float('inf')] * len(nums) ##这里是提前规定指定长度的列表，不用numpy也可以
        ans_pointer = right

        while left <= right:
            if abs(nums[left]) < abs(nums[right]):
                ans[ans_pointer] = int(nums[right] ** 2)
                right -= 1
            elif abs(nums[left]) >= abs(nums[right]):
                ans[ans_pointer] = int(nums[left] ** 2)
                left += 1
            print(ans)
            print("left",left)
            print("right",right)
            ans_pointer -= 1
        
        return ans
    
class Solution_3(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 0
        right = len(nums) - 1
        ans = []

        while left <= right:
            if abs(nums[left]) < abs(nums[right]):
                ans.append(int(nums[right] ** 2))
                right -= 1
            elif abs(nums[left]) >= abs(nums[right]):
                ans.append(int(nums[left] ** 2))
                left += 1
            print(ans)
            print("left",left)
            print("right",right)
        
        return ans[::-1]

nums = [-4,-1,0,3,10]
solution = Solution_3()
ans = solution.sortedSquares(nums)
print(ans)
