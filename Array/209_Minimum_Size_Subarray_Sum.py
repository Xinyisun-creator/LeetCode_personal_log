class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        ans = ans = float('inf')
        sum = 0

        while right < len(nums):          
            sum += nums[right]
            while sum >= target:
                ans = min(ans, (right - left + 1))
                sum -= nums[left]
                left += 1
            
            right += 1
        return ans if ans != float('inf') else 0

nums = [2,3,1,2,4,3]
target = 7
solution = Solution()
ans = solution.minSubArrayLen(target,nums)
print(ans)

class Solution_2(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        left = 0
        right = 0
        min_l = float('inf')
        cur_sum = 0

        while right < len(nums):
            cur_sum += nums[right]

            while cur_sum >= target:
                min_l = min(min_l,right - left + 1)
                cur_sum -= nums[left]
                left += 1
            
            right += 1
        
        return min_l if min_l != float('inf') else 0

