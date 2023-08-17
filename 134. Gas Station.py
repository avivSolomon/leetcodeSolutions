from typing import List
class Solution:
	def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
		if sum(gas) - sum(cost) < 0:
			return -1
		n = len(gas)
		sm, index = [], []
		for i in range(n):
			if gas[i] - cost[i] >= 0:
				index.append(i)
			sm.append(gas[i] - cost[i])

		for i in index:
			way = sm[i:] + sm[:i]
			tank = 0
			for j in range(n):
				tank += way[j]
				if tank < 0:
					break
				elif j == n - 1:
					return i
		return -1