class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        output = [[None for i in range(n)]for j in range(n)]
        direction = "right" #right down left up
        left_edge = 0
        right_edge = n-1
        down_edge = n-1
        up_edge = 0

        j_ = 0

        for i in range(1,n**2+1):
            if direction == "right":
                output[left_edge][j_] = i
            elif direction == "down":
                output[j_][right_edge] = i
            elif direction == "left":
                output[down_edge][j_] = i
            elif direction == "up":
                output[j_][left_edge] = i

            if direction == "right" and j_ >= right_edge:
                direction = "down"
                j_ = up_edge
            elif direction == "down" and j_ >= down_edge:
                # import pdb; pdb.set_trace()
                direction = "left"
                j_ = right_edge
            elif direction == "left" and j_ <= left_edge:
                direction = "up"
                j_ = down_edge
                up_edge += 1
            elif direction == "up" and j_ <= up_edge:
                # import pdb; pdb.set_trace()
                j_ = left_edge
                direction = "right"
                right_edge -= 1
                down_edge -= 1
                left_edge += 1
            
            if direction == "right" or direction == "down":
                j_ += 1
            else:
                j_ -= 1
            
            print("direction: ", direction)
            print("j_:", j_)
            print("output: ")
            print(output)
            print()
        
        return output

n = 3
solution = Solution()
ans = solution.generateMatrix(n=3)
print(ans)