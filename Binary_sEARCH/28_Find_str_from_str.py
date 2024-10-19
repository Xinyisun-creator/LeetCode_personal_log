class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        left = 0
        while left < (len(haystack) - len(needle) + 1):
            if haystack[left] == needle[0]:
                j = 1
                right = left + 1
                while j <= len(needle) - 1:
                    if haystack[right] == needle[j] and j < len(needle) - 1:
                        right += 1
                        j += 1
                    elif haystack[right] == needle[j] and j == len(needle) - 1:
                        return left
                    else:
                        break
            left += 1
        return -1
    
class Solution_KMP(object):
    def toNext(self,next,needle):
        j = 0
        
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        left = 0
        while left < (len(haystack) - len(needle) + 1):
            if haystack[left] == needle[0]:
                j = 1
                right = left + 1
                while j <= len(needle) - 1:
                    if haystack[right] == needle[j] and j < len(needle) - 1:
                        right += 1
                        j += 1
                    elif haystack[right] == needle[j] and j == len(needle) - 1:
                        return left
                    else:
                        break
            left += 1
        return -1

if __name__ == '__main__':
    haystack = "leetcode"
    needle = "leeto"
    print(Solution().strStr(haystack, needle))