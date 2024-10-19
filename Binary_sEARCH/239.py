# from collections import deque
# class Solution(object):
#     def maxSlidingWindow(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: List[int]
#         """
#         window = deque()
#         ans = []
#         for i in range(k-1,len(nums)):
#             if i == k-1:
#                 for j in range(k-1):
#                     window.append(nums[j])
#             else:
#                 window.popleft()
#                 window.append(nums[i])
            
#             ans.append(max(window))
        
#         return ans


from collections import deque

class MyDeque():
    def __init__(self):
        self.queue = deque()
    
    def pop(self,value):
        if self.queue and value == self.queue[0]:
            self.queue.popleft()
    
    def push(self,value):
        while self.queue and self.queue[0] <= value:
            self.queue.popleft()
        self.queue.append(value)
    
    def front(self):
        while self.queue:
            return self.queue[0]
    
class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = MyDeque()
        ans = []
        for j in range(k):
            dq.push(nums[j])
        max_v = dq.front()
        ans.append(max_v)
        for i in range(k,len(nums)):
            dq.pop(nums[i-k])
            dq.push(nums[i])
            max_v = dq.front()
            print("nums[i-k]",nums[i-k])
            print("max_v",max_v)
            ans.append(max_v)
        return ans

nums = [1,3,-1,-3,5,3,6,7]
k = 3
solution = Solution()
print(solution.maxSlidingWindow(nums, k))  # Output: [3,3,5,5,6,7]
