class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        temp = []
        for i in tokens:
            if i in "+-*/":
                b = int(temp.pop())
                a = int(temp.pop())
                if i == "+":
                    ans = a + b
                elif i == "/":
                    ans = int(a/b)
                elif i == "-":
                    ans = a - b
                elif i == "*":
                    ans = a * b
                temp.append(ans)
            else:
                temp.append(int(i))
        
        return temp[0]
    
solution = Solution()    
# tokens1 = ["2", "1", "+", "3", "*"]
# print(solution.evalRPN(tokens1))  # Output: 9

# # Example 2: Division and negative numbers
# tokens2 = ["4", "13", "5", "/", "+"]
# print(solution.evalRPN(tokens2))  # Output: 6

# Example 3: Complex expression
tokens3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(solution.evalRPN(tokens3))  # Output: 22