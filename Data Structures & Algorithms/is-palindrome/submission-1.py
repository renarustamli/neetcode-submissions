class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_s = ""
        for alp in s:
            if alp.isalnum():
                new_s += alp
        if new_s ==  new_s[::-1]:
            return True
        return False