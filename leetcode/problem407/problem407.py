def spe(*vars):
    for var in vars:
        print(var)
    exit()

class Solution:
    
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """

        h, w = len(heightMap), len(heightMap[0])
        i, j = 1, 1

        while 1 <= i and i <= h-2:
            while 1 <= j and j <= w-2:
                self.allAroundAreHigher(heightMap, i, j)

    def allAroundAreHigher(self, heightMap, i, j):
        
        around = []
        DIRECTION = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # 是否下降
        for k in range(len(DIRECTION)):
            around_h = heightMap[i+DIRECTION[k][0]][j+DIRECTION[k][0]] 
            # 比自己大的加入around数组
            if  around_h > heightMap[i][j]:
                around.append(around_h)
            # 比自己小的往下搜索，继续寻找边界around
            else:

                water_line = min(around)
                print('水位线:', water_line)

if __name__ == "__main__":
    
    heightMap = [[1,4,3,1,3,2],
                 [3,2,1,3,2,4],
                 [2,3,3,2,3,1]]
              
    solution = Solution()
    result = solution.trapRainWater(heightMap)
    print(result)
