class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        st = []
        ts = ""
        for c in s:
            if c == " ":
                st.append(ts)
                ts = ""
            else:
                ts += c
        st.append(ts)
        for w in st:
            ans.append(w[::-1])
        
        return " ".join(ans)