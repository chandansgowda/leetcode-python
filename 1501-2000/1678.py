class Solution:
    def interpret(self, command: str) -> str:
        d = {"G":"G","()":"o","(al)":"al"}

        t = ""
        res = ""

        for i in range(len(command)):
            t += command[i]
            if t in d:
                res += d[t]
                t = ""

        return res
        
