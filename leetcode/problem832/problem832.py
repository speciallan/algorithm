class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        # 0 1 2 3 4 5
        for k,v in enumerate(A):

            length = len(v)

            # 翻转
            for k2,v2 in enumerate(v):

                if k2 >= length/2:
                    break

                temp = v2
                A[k][k2] = A[k][length-1-k2]
                A[k][length-1-k2] = temp

            # 反转
            for k2,v2 in enumerate(v):
                
                A[k][k2] = 1 - A[k][k2]

        return A

if __name__ == "__main__":

    img = [[1,1,0],[1,0,1],[0,0,0]]
    img = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    print(img)

    solution = Solution()
    out = solution.flipAndInvertImage(img)

    print(out)