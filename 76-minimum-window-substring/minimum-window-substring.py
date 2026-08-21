from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = Counter(t)
        left = 0
        count = len(t)

        min_len = float("inf")
        start = 0

        for right in range(len(s)):

            # Expand window
            if s[right] in need:
                if need[s[right]] > 0:
                    count -= 1

                need[s[right]] -= 1

            # Shrink window while valid
            while count == 0:

                # Update minimum window
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                # Remove left character
                if s[left] in need:
                    need[s[left]] += 1

                    if need[s[left]] > 0:
                        count += 1

                left += 1

        return "" if min_len == float("inf") else s[start:start + min_len]