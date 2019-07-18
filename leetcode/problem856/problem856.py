#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Speciallan

class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """

        if len(S) == 0:
            return 0

        S = S.replace('()', '1')
        arr = []
        total = 0

        for i in range(0, len(S)):

            if S[i] == '(':
                arr.append(total)
                total = 0
            elif S[i] == ')':
                total = total *2 + arr.pop()
            else:
                total += int(S[i])

        return total



if __name__ == "__main__":

    S = "(()(()))"

    solution = Solution()
    result = solution.scoreOfParentheses(S)
    print(result)