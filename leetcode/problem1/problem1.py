
import time

# 遍历 0.00358 ms
class Solution:

    def twoSum(self, nums, target):

        result = []
        for k, v in enumerate(nums):
            for k2, v2 in enumerate(nums):
                if v + v2 == target and k < k2:
                    result = [k, k2]

        return result

# 两遍hash 0.005723
class Solution2:

    def twoSum(self, nums, target):

        result = []
        sub = {}
        for k, v in enumerate(nums):
            sub[v] = k

        for k, v in enumerate(nums):
            t = target - v
            if t in sub.keys() and k < sub[t]:
                result = [k, sub[t]]
        
        return result

# 一遍hash
class Solution3:

    def twoSum(self, nums, target):

        result = []
        sub = {}
        for k, v in enumerate(nums):

            t = target - v

            if t in sub.keys():
                if k < sub[t]:
                    result = [k, sub[t]]
                    break
                elif k > sub[t]:
                    result = [sub[t], k]
                    break
            else:
                sub[v] = k
        
        return result

if __name__ == '__main__':

    nums = [2, 7, 11, 15]
    target = 9

    # nums = [3, 2, 4]
    # target = 6
    nums = [3, 3]
    target = 6

    start_time = time.time()

    # solution = Solution()
    solution = Solution3()
    result = solution.twoSum(nums, target)

    used_time =  time.time() - start_time
    print(result)
    print(round(used_time * 1000, 5))
