import numpy as np

def spe(*vars):
    for var in vars:
        print(var)
    exit()

class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left = right = h = 0
        water_amount = np.array([])

        i = 0

        # 去掉所有左边为0的
        if height[i] == 0: 
            i += 1

        while i < len(height):

            finish = False
            left = i
            h = height[left]

            for j in range(i+1, len(height)):

                # 如果水位往下走
                if height[j] < h:
                    continue

                # 如果右高度到水位线
                else:
                    right = j
                    finish = True
                    break
            
            if finish:

                amount = np.array([])
                for j in range(left+1, right):
                    amount = np.append(amount, h - height[j])

                sum1 = amount.sum()
                print(amount)
                water_amount = np.append(water_amount, sum1)

                # 还原变量
                i = right
                finish = False
            
            else:
                i = len(height)

        return water_amount.sum()

class Solution2:

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        _height = height[1:-1]        
        if not _height:
            return 0

        hmax = max(_height)
        hmin = min(height[0], height[-1])

        if hmax < hmin:
            return hmin*len(_height) - sum(_height)
        
        pos = _height.index(hmax)+1

        return self.trap(height[:pos+1]) + self.trap(height[pos:])

if __name__ == "__main__":

    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    solution = Solution2()
    result = solution.trap(height)
    print(result)