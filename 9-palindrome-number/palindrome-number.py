class Solution:
    def isPalindrome(self, x: int) -> bool:
        #turn into string
        s = str(x)

        return s==s[::-1]