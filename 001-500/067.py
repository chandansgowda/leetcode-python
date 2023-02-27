class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = 0
        la = len(a)-1
        lb = len(b)-1
        res = ""

        while la>=0 or lb>=0:
            s = c
            if la>=0 : s += ord(a[la]) - ord('0')
            if lb>=0 : s += ord(b[lb]) - ord('0')
            la,lb = la-1, lb-1
            c = 1 if s>1 else 0
            res += str(s%2)

        if c==1:
            res+="1"

        return res[::-1]
    
    
    
 class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        i,j,c = len(a)-1,len(b)-1,0
        while i>=0 or j>=0:
            sum = c
            if i>=0:
                sum+=int(a[i])
            if j>=0:
                sum+=int(b[j])
            i,j = i-1,j-1
            c = 1 if sum>1 else 0
            res = str(sum%2) + res
            
        if c: res = "1"+res
        return res
        
        
        
        
 class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = 0
        la = len(a)-1
        lb = len(b)-1
        res = ""

        while la>=0 or lb>=0:
            s = c
            if la>=0 : s += int(a[la])
            if lb>=0 : s += int(b[lb])
            la,lb = la-1, lb-1
            c = 1 if s>1 else 0
            res += str(s%2)

        if c==1:
            res+="1"

        return res[::-1]
            
                
 
