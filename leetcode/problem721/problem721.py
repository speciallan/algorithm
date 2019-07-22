#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Speciallan

class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        emails, merged_emails = {}, []
        existed = []
        for k,v in enumerate(accounts):
            # print(k,v)
            if k not in existed:
                in_emails = False
                for k2,v2 in enumerate(v[1:]):
                    if v2 not in emails:
                        # 存放序号
                        emails[v2] = [k]
                        # existed.append(k)

                    else:
                        emails[v2].append(k)
                        # existed.append(k)
                    break


        print(emails)

        for k,v in emails.items():
            name, ids = accounts[v[0]][0], v

            line = [name]

            for k2,v2 in enumerate(ids):
                for k3,v3 in enumerate(accounts[v2][1:]):
                    if v3 not in line:
                        line.append(v3)

            merged_emails.append(line)
            line.sort()

        # print(emails)
        # print(merged_emails)
        return merged_emails

if __name__ == "__main__":

    # 是个深搜问题，这里没搞定，数据结构没问题
    accounts = [["John", "johnsmith@mail.com", "john00@mail.com"],
                ["John", "johnnybravo@mail.com"],
                ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                ["Mary", "mary@mail.com"]]

    accounts = [["Alex","Alex5@m.co","Alex4@m.co","Alex0@m.co"],["Ethan","Ethan3@m.co","Ethan3@m.co","Ethan0@m.co"],["Kevin","Kevin4@m.co","Kevin2@m.co","Kevin2@m.co"],["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe2@m.co"],["Gabe","Gabe3@m.co","Gabe4@m.co","Gabe2@m.co"]]

    solution = Solution()
    result = solution.accountsMerge(accounts)
    print(result)
