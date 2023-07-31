from typing import List

class DisJointSet:
    def __init__(self, n):
        self.size = [1 for _ in range(n+1)]
        self.parent = [i for i in range(n+1)]

    def find_ultimate_parent(self, node):
        if node == self.parent[node]:
            return node
        
        ultimate_parent = self.find_ultimate_parent(self.parent[node])
        self.parent[node] = ultimate_parent
        return self.parent[node]

    def union_by_size(self, u, v):
        ulp_u = self.find_ultimate_parent(u)
        ulp_v = self.find_ultimate_parent(v)

        if ulp_u == ulp_v:
            return
        
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        ds = DisJointSet(n)
        result = []

        mail_map = dict()
        for i in range(n):
            for j in range(1, len(accounts[i])):
                if accounts[i][j] not in mail_map:
                    mail_map[accounts[i][j]] = i
                else:
                    ds.union_by_size(i, mail_map[accounts[i][j]])
        
        mail_list = [[] for _ in range(n)]
        for key in mail_map:
            mail = key
            node = mail_map[mail]
            ulp_node = ds.find_ultimate_parent(node)
            mail_list[ulp_node].append(mail)

        for k in range(n):
            if mail_list[k]:
                account = []
                name = accounts[k][0]
                account = [name]
                mails = mail_list[k]
                mails.sort()
                account.extend(mails)
                result.append(account)

        return result
