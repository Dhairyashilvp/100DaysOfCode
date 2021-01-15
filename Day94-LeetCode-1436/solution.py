class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = []
        for p in paths:
            if p[1] in d:
                d.remove(p[1])
            if p[0] in d:
                d.remove(p[0])
            else:
                d.append(p[1])
            
        return(d[0])
        # A, B = map(set, zip(*paths))
        # return (B - A).pop()
        
            