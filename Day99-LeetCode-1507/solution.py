class Solution:
    def reformatDate(self, date: str) -> str:
        Month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]      
        return "{:04d}-{:02d}-{:02d}".format(int(date[-4:]), (Month.index(date[-8:-5])+1), int(date[:-11]))