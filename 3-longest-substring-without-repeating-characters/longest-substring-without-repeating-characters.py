class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}        
        maxLength = 0      
        left = 0           

        for i, char in enumerate(s):
            if char in seen:
                # move left past the previous duplicate
                left = max(left, seen[char] + 1)

            seen[char] = i  # remember latest position of char

            current = i - left + 1  # length of current window
            maxLength = max(maxLength, current)  # keep the biggest length

        return maxLength  # answer after checking entire string