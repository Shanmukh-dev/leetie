# ──────────────────────────────────────────────────
# Problem  : 547. Number of Provinces
# Difficulty: Medium
# Tags     : Depth-First Search, Breadth-First Search, Union-Find, Graph Theory
# Link     : https://leetcode.com/problems/number-of-provinces/
# Runtime  : N/A (beats 0%)
# Memory   : N/A (beats 0%)
# Language : python3
# Copyright: (c) 2026 Shanmukh-dev. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = defaultdict(list)

        for i in range(n):
            for j in range(n):
                print(i+1, j+1, isConnected[i][j])
                if i == j:
                    if not graph.get(i+1):
                        graph[i+1] = []

                elif isConnected[i][j] == 1:
                    graph[i+1].append(j+1)

        
        q = deque([1])
        vis = set()

        while q:
            node = q.popleft()
            vis.add(node)
            for i in graph(node):
                



                
        print(graph)