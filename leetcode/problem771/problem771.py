import time

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """

        total = 0
        for i in J:
            for j in S: 
                if i == j:
                    total += 1

        return total

if __name__ == "__main__":

    J = "aA"
    S = "aAAbbbb"

    s = Solution()
    result = s.numJewelsInStones(J, S)

    print(result)