class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
    
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])  # Path compression
        return self.parent[node]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False
        
        if self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = self.parent[u]
        elif self.rank[root_v] > self.rank[root_u]:
            self.parent[root_u] = self.parent[root_v]
        else:
            self.parent[root_u] = self.parent[root_v]
            self.rank[root_u] += 1
        
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))

        emailToAcc = {} # email - > index of account 
        emailGroup = defaultdict(list) # index of acc -> list of emails
        output = []

        # check all emails and map to their account index
        # if any email repeats that means the existing account and new account should be same
        for i, emails in enumerate(accounts):
            for e in emails[1:]: # email[0] is the name
                if e in emailToAcc: # if same emails then it should belong to same parent
                    uf.union(i, emailToAcc[e]) # union so that they have same parent
                else:
                    emailToAcc[e] = i
        
        # Group all the account indexes, each index will have a list of emails associated
        for e, i in emailToAcc.items():
            leader = uf.find(i) # parent of this account 
            emailGroup[leader].append(e)
        
        # print in format
        for i, emails in emailGroup.items():
            name = accounts[i][0] # get the name of the account by its index
            output.append([name] + sorted(emails)) # we need emails in sorted order
        
        return output
        

