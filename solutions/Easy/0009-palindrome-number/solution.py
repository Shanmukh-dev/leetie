# ──────────────────────────────────────────────────
# Problem  : 9. Palindrome Number
# Difficulty: Easy
# Tags     : Math
# Link     : https://leetcode.com/problems/palindrome-number/
# Runtime  : 13 ms (beats 23%)
# Memory   : 19196000 (beats 87%)
# Language : python3
# Copyright: (c) 2026 Shanmukh-dev. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:

    def isPalindrome(self, x: int) -> bool:
        x = str(x)

        return x[::-1] == x

        