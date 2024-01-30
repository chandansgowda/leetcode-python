class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()  
                if token=="+":
                    c = a+b
                elif token=="-":
                    c = a-b
                elif token=="/":
                    c = int(a/b)
                elif token=="*":
                    c = a*b
                stack.append(c)
                
        return stack[-1]


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        x = "+-*/"
        for token in tokens:
            if token not in x:
                s.append(int(token))
            else:
                a = s.pop()
                b = s.pop()
                if token=="+":
                    s.append(a+b)
                elif token=="-":
                    s.append(b-a)
                elif token=="*":
                    s.append(a*b)
                else:
                    s.append(int(b/a))
        return s[0]
