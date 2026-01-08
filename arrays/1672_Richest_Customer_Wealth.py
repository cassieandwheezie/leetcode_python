class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth =[]
        e=0
        for i in accounts:
            e=0
            for j in i:
                e=e+j
                wealth.append(e)
        return max(wealth)
