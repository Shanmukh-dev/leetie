# ──────────────────────────────────────────────────
# Problem  : 8. String to Integer (atoi)
# Difficulty: Medium
# Tags     : String
# Link     : https://leetcode.com/problems/string-to-integer-atoi/
# Runtime  : N/A (beats 0%)
# Memory   : N/A (beats 0%)
# Language : python3
# Copyright: (c) 2026 Shanmukh-dev. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution:
    def clamp32Bit(self, num):
        max_int = 2**31 - 1
        min_int = -2**31 

        if num > max_int:
            return max_int
        elif num < min_int:
            return min_int
        else:
            return num
    def myAtoi(self, s: str) -> int:
        result = 0
        # i = 0
        sign = 1

        if s and (not s.isspace()):
            while s[0].isspace():
                s = s[1::]
                print(s)
                # i+=1

            else:
                if s[0] == "-":
                    sign = -1
                    s = s[1::]
                elif s[0] == "+":
                    s = s[1::]
                    
                # print(s)
                for i in s:
                    if i.isdigit():
                        result = result * 10 + (ord(i) - ord("0"))
                    else:
                        break

            
        result *= sign
        result = self.clamp32Bit(result)


        return result 
        