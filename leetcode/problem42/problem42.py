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

        if len(height) == 0:
            return 0

        left = right = h = 0
        water_amount_left = {}

        i = 0

        # 去掉所有左边为0的
        while height[i] == 0 and i+1 < len(height): 
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

                amount = []
                for j in range(left, right):
                    amount.append(h - height[j])

                sum1 = sum(amount)
                water_amount_left[str(left) + '-' + str(right)] = sum1
                print(water_amount_left)

                # 还原变量
                i = right
                finish = False
            
            else:
                i = len(height)

        left = right = h = 0
        water_amount_right = {}

        # 从右往左
        i = len(height) - 1

        # 去掉所有右边为0的
        while height[i] == 0 and i >= 0: 
            i -= 1

        while i >= 0:

            finish = False
            right = i
            h = height[right]

            for j in range(i-1, -1, -1):

                # 如果水位往下走
                if height[j] < h:
                    continue

                # 如果左高度到水位线
                else:
                    left = j
                    finish = True
                    break
            
            if finish:

                amount = []
                for j in range(right, left, -1):
                    amount.append(h - height[j])

                sum1 = sum(amount)
                water_amount_right[str(left) + '-' + str(right)] = sum1
                print(water_amount_right)

                # 还原变量
                i = left
                finish = False
            
            else:
                i = -1

        # 排除重复
        water_amount = {}
        for k,v in water_amount_left.items():
            water_amount[k] = v

        for k,v in water_amount_right.items():
            if not water_amount.get(k):
                water_amount[k] = v

        total_water = 0
        for k, v in water_amount.items():
            total_water += v

        return total_water

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

        ###
        return self.trap(height[:pos+1]) + self.trap(height[pos:])

if __name__ == "__main__":

    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    # height = []
    # height = [0]
    # 重复情况
    # height = [0, 0, 0, 1, 0, 1, 0]
    # height = [4, 2, 3]

    solution = Solution()
    result = solution.trap(height)
    print(result)