# ──────────────────────────────────────────────────
# Problem  : 9. Palindrome Number
# Difficulty: Easy
# Tags     : Math
# Link     : https://leetcode.com/problems/palindrome-number/
# Runtime  : 0 ms (beats 100%)
# Memory   : 19492000 (beats 19%)
# Language : python3
# Copyright: (c) 2026 Shanmukh-dev. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:

    def isPalindrome(self, x: int) -> bool:
        x = str(x)

        return x[::-1] == x

        