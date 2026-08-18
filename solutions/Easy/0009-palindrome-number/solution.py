# ──────────────────────────────────────────────────
# Problem  : 9. Palindrome Number
# Difficulty: Easy
# Tags     : N/A
# Link     : https://leetcode.com/problems/palindrome-number/
# Runtime  : N/A (beats 0%)
# Memory   : N/A (beats 0%)
# Language : python3
# Copyright: (c) 2026 Shanmukh-dev. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:

    def isPalindrome(self, x: int) -> bool:
        x = str(x)

        return x[::-1] == x

        