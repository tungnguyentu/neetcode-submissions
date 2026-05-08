class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_s = "".join(s.split()).lower()
        trim_s = []
        for c in lower_s:
            if c.isnumeric() or c.isalpha():
                trim_s.append(c)
        s = "".join(trim_s)
        return s == s[::-1]