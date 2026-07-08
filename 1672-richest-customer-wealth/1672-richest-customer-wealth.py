class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        Richest_amount = 0
        
        for i in accounts:
            total_amount = 0
            for j in i:
                total_amount +=j
            if Richest_amount< total_amount:
                Richest_amount = total_amount
        return Richest_amount