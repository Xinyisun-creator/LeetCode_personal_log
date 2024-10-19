class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        slow = 0
        fast = 0
        while fast < len(nums):
            if nums[fast] == val:
                print("pace slow")
                fast += 1
            else:
                print("pace same")
                nums[slow] = nums[fast]
                slow += 1
                fast += 1
        return slow,nums

nums = [2]
val = 3
solution = Solution()
ans,list = solution.removeElement(nums,val)
print(ans)
print(list)