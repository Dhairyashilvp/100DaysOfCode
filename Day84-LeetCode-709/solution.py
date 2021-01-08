# class Solution:
#     def toLowerCase(self, str: str) -> str:
#         return str.lower()
class Solution:
    def toLowerCase(self, str: str) -> str:
        ans = ""
        for c in str :
            if ord(c) >= 65 and ord(c) <= 90:
                ans += chr(ord(c)+32)
            else:
                ans += c
        return ans