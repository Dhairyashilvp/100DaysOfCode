class Solution:
    def reformatNumber(self, number: str) -> str:
        b = []
        ans = ""
        # for d in number:
        #     if d != " " and d != "-":
        #         b+=d
        # print(b)
        # if len(b) % 3 == 0:
        #     return "-".join([b[i:i+3] for i in range(0,len(b),3)]) 
        # else:
        #     for i in range(0, len(b)-4,3):
        #         ans += b[i:i+3] + "-"
        #     if len(b) - len(ans) == 4:
        #         ans += b[len(ans)+1:len(ans)+3] + "-" + b[len(ans)+3:]
        #     else:
        #         ans += b[len(ans)+1:]
        # print(ans)
        for d in number:
            if d != " " and d != "-":
                b.append(d)
        i = 0
        while(i < len(b)-4):
            b.insert(i+3, '-')
            i+=4
        
        if (len(b) - i == 4) :
            b.insert(i+2, '-')

        return "".join(b)