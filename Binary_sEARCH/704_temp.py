class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        reg = float('inf')
        sum = 0 + nums[0]

        while right <= len(nums) - 1:
            if sum < target:
                right += 1
                sum += nums[right]
            elif sum > target:
                sum -= nums[left]
                left += 1
            else:
                reg = min(reg,sum)
                right += 1
                sum += nums[right]
                sum -= nums[left]
                left += 1
        return reg
print(Solution().minSubArrayLen(7,[2,3,1,2,4,3]))