# from leetcode.spe import *

def spe(*vars):
    for var in vars:
        print(var)
    exit()

class Solution(object):

    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """

        h, w = len(A), len(A[0])
        h2, w2 = h * 2 + (h - 1) - 1, w * 2 + (w - 1) - 1
        # spe(h, w)

        # 填充A
        A_padding = []
        
        for i in range(h2):

            temp = []
            for j in range(w2):

                if h-1 <= i and i <= (h-1)*2 and w-1 <= j and j <= (w-1)*2:
                    try:
                        temp.append(A[i-h+1][j-w+1])
                    except IndexError as identifier:
                        spe('这里出错了1: ',identifier, i-h+1, j-w+1)
                else:
                    temp.append(0)

            A_padding.append(temp)

        # print
        for i in range(len(A_padding)):
            print(A_padding[i])

        # 求卷积
        conv_arr = []

        for i in range(h2-h+1):
            for j in range(w2-w+1):

                conv = 0
                for m in range(h):
                    for n in range(w):
                        try:
                            conv += A_padding[i+m][j+n] * B[m][n]
                        except IndexError as identifier:
                            spe('这里出错了2:', identifier, i, m, i+m, j+n)

                conv_arr.append(conv)

        conv_arr.sort()
        print(conv_arr)
        max_conv = conv_arr[-1]

        return max_conv

    def calConv(self, A, B):
        pass

class Solution2(object):

    def largestOverlap(self, A, B):

        import numpy as np

        # from  warnings import filterwarnings
        # filterwarnings("ignore")

        def conv2D(img, kernel):

            import numpy as np

            A, kernel = np.array(img), np.array(kernel)

            h, w = A.shape
            n, _ = kernel.shape
            # spe(h, w)

            # 填充A
            A_padding = np.zeros([h+2*(n-1), w+2*(n-1)])
            A_padding[n-1:n-1+h, n-1:n-1+w] = A[0:h, 0:w]

            # print
            # for i in range(len(A_padding)):
            #     print(A_padding[i])

            h_result, w_result = h+n-1, w+n-1
            result = np.zeros([h_result, w_result])

            for i in range(h_result):
                for j in range(w_result):
                    
                    temp = A_padding[i:i+n, j:j+n]
                    # spe(temp.shape, kernel.shape)

                    try:
                        temp = np.multiply(temp, kernel)
                    except Exception as identifier:
                        spe(identifier, i, j, n, temp, temp.shape, kernel.shape)

                    result[i][j] = temp.sum()

            return result

        conv = conv2D(A, B)
        max_conv = int(np.max(conv))

        return max_conv

class Solution3(object):
    def largestOverlap(self, A, B):

        import collections

        N = len(A)
        LA = [i / N * 100 + i % N for i in range(N * N) if A[i/N][i%N]]
        LB = [i / N * 100 + i % N for i in range(N * N) if B[i/N][i%N]]
        c = collections.Counter(i - j for i in LA for j in LB)
        return max(c.values() or [0])
       
if __name__ == "__main__":

    A = [[1, 1, 0],
         [0, 1, 0],
         [0, 1, 0]]

    B = [[0, 0, 0],
         [0, 1, 1],
         [0, 0, 1]]

    # A = [[0]]

    solution = Solution()
    # solution = Solution3()

    # solution1: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 3]
    # solution2: 
    result = solution.largestOverlap(A, B)
    print("result:%i" % result)
