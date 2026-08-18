// ──────────────────────────────────────────────────
// Problem  : 547. Number of Provinces
// Difficulty: Medium
// Tags     : Depth-First Search, Breadth-First Search, Union-Find, Graph Theory
// Link     : https://leetcode.com/problems/number-of-provinces/
// Runtime  : 6 ms (beats 5%)
// Memory   : 48484000 (beats 23%)
// Language : java
// Copyright: (c) 2026 Shanmukh-dev. All rights reserved.
// Synced by: leetie
// ──────────────────────────────────────────────────

class Solution {
    void dfs(Map<Integer, List<Integer>> adj, int node, int[] visit){
        visit[node] = 1;

        for(int it: adj.get(node)){
            if(visit[it] != 1)
                dfs(adj, it, visit);
        }
    }
    public int findCircleNum(int[][] isConnected) {
        Map<Integer, List<Integer>> adj = new HashMap<>();
        int n = isConnected.length;
        for(int i = 0; i < n; i++){
            adj.put(i, new ArrayList<>());
        }

        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(isConnected[i][j] == 1 && i != j){
                    adj.get(i).add(j);
                    adj.get(j).add(i);
                }
            }
        }

        int[] visit = new int[n];
        int cnt = 0;
        for(int i = 0; i < n; i++){
            if(visit[i] != 1) {
                dfs(adj, i, visit);
                cnt++;
            }
        }

        return cnt;
    }
}