class Solution:
    def maximum69Number (self, num: int) -> int:
      nl = list(str(num))
      for i in range(len(nl)):
        if nl[i]=='6':
          nl[i]= '9'
          break
      return int(''.join(nl))
        
