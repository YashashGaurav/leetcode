"""
	1584. Min Cost to Connect All Points
"""

from typing import List
import math
import heapq


class Solution:
	def minCostConnectPoints0(self, points: List[List[int]]) -> int:

		sum = 0

		for u_x, u_y in points:
			min_dist = math.inf
			temp = set()
			for v_x, v_y in points:
				if (u_x, u_y) != (v_x, v_y):
					dist = abs(u_x - v_x) + abs(u_y - v_y)
					if dist < min_dist:
						min_dist = min(min_dist, dist)
						temp = (v_x, v_y)

			sum += min_dist

		return sum

	def minCostConnectPoints1(self, points: List[List[int]]) -> int:
		minHeap = []

		for ux, uy in points:
			for vx, vy in points:
				if (ux, uy) != (vx, vy):
					heapq.heappush(
						minHeap, 
						((abs(ux - vx) + abs(uy - vy)), [(ux, uy), (vx, vy)])
					)

		nodes = set()
		min_dist = 0
		while len(nodes) < len(points) and len(minHeap) > 0:
			dist, adj_points = heapq.heappop(minHeap)
			if adj_points[0] in nodes: # and adj_points[1] in nodes:
				continue
			else:
				nodes.add(adj_points[0])
				# nodes.add(adj_points[1])
				min_dist += dist

		return min_dist


	# Accepted	2060 ms	98.3 MB
	# but not the right way to implement MST - we are not tracking where
	# and edge originated from - it does not matter for us right now,
	# though most questions will ask us to.
	def minCostConnectPoints(self, points: List[List[int]]) -> int:
		minHeap = []
		visited = set()

		min_dist = 0

		heapq.heappush(
			minHeap, 
			(0, tuple(points[0]))
		)
		

		while len(visited) < len(points): # MST has n-1 edges	
			
			dist, point_to = heapq.heappop(minHeap)

			if point_to in visited:
				continue
			
			min_dist += dist

			visited.add(point_to)

			for vx, vy in points:
				if (vx, vy) not in visited:
					heapq.heappush(
						minHeap, 
						((abs(point_to[0] - vx) + abs(point_to[1] - vy)), (vx, vy))
					)
			

		return min_dist


print(Solution().minCostConnectPoints([[3,12],[-2,5],[-4,1]]))
print(Solution().minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]])) # 20
print(Solution().minCostConnectPoints([[0,0]]))
print(Solution().minCostConnectPoints([[2,-3],[-17,-8],[13,8],[-17,-15]]))


