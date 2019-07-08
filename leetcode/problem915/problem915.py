#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Speciallan

class Solution(object):
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        left = []
        right = []

        maxl = -99999999
        minr = 99999999

        for i in range(0, len(A)):
            if A[i] > maxl:
                maxl = A[i]
                left.append(maxl)
            else:
                left.append(maxl)

        for i in range(len(A)-1, -1, -1):
            if A[i] < minr:
                minr = A[i]
                right.append(minr)
            else:
                right.append(minr)

        right.reverse()
        print(left)
        print(right)

        i = len(A)-1
        cut = i

        while i>=1:

            if left[i-1] <= right[i]:
                cut = i-1
                print(cut)
                i -= 1
            else:
                i -= 1

        return cut+1

if __name__ == '__main__':

    A = [5,0,3,8,6]
    A = [1,1,1,0,6,12]
    # A = [1,1]
    # A = [26,51,40,58,42,76,30,48,79,91]

    s = Solution()
    result = s.partitionDisjoint(A)

    print(result)



