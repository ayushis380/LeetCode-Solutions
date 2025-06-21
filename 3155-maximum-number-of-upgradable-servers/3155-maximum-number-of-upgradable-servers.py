class Solution:
    def maxUpgrades(self, count: List[int], upgrade: List[int], sell: List[int], money: List[int]) -> List[int]:
        """
        For each item, determine the maximum number of upgrades possible.
        You can sell some of the items to make money to afford the upgrades.
        """
        n = len(count)
        answer = [-1] * n

        for i in range(n):
            total_upgrade_cost = count[i] * upgrade[i]

            # If we can afford upgrading all items without selling
            if total_upgrade_cost <= money[i]:
                answer[i] = count[i]
                continue

            # Binary search to find maximum number of items we can upgrade
            # by possibly selling some of them
            low, high = 1, count[i]

            while low <= high:
                sold = (low + high) // 2
                upgraded = count[i] - sold

                # Total upgrade cost for upgraded items
                cost = upgraded * upgrade[i]
                # Total money available after selling 'sold' items
                available_money = (sold * sell[i]) + money[i]

                if cost <= available_money:
                    # It's possible to upgrade 'upgraded' items
                    answer[i] = max(answer[i], upgraded)
                    # Try to sell fewer items to upgrade more
                    high = sold - 1
                else:
                    # Not enough money, need to sell more items
                    low = sold + 1

        return answer