class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        costs = sorted(costs, key=lambda cost: cost[0] - cost[1])
        total = 0
        for cost in costs[:n]:
            total += cost[0]
        for cost in costs[n:]:
            total += cost[1]
        return total
