class Solution:
    def intToRoman(self, num: int) -> str:
        values=[["I",1],["IV",4],["V",5],["IX",9],["X",10],["XL",40],["L",50],
        ["XC",90],["C",100],["CD",400],["D",500],["CM",900],["M",1000]]
        s=""
        for char,val in reversed(values):
            # print(char,val)
            if(num//val!=0):
                count=num//val
                s+=(char*count)
                num=num%val
        return s