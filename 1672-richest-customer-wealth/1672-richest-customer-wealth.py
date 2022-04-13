class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0
        for account in accounts:
            currentWealth = 0
            for wealth in account:
                currentWealth += wealth
            maxWealth = max(maxWealth,currentWealth)
        return maxWealth