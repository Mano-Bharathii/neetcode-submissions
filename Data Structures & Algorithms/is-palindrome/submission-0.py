class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = "".join([x for x in s if x.isalnum()]).lower()
        return new_s == new_s[::-1]