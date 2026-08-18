# ──────────────────────────────────────────────────
# Problem  : 9. Palindrome Number
# Difficulty: Easy
# Tags     : Math
# Link     : https://leetcode.com/problems/palindrome-number/
# Runtime  : 1 ms (beats 93%)
# Memory   : 19408000 (beats 19%)
# Language : python3
# Copyright: (c) 2026 Shanmukh-dev. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:

    def isPalindrome(self, x: int) -> bool:
        x = str(x)

        return x[::-1] == x

        