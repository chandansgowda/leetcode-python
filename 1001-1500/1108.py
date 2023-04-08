class Solution:
    def defangIPaddr(self, address: str) -> str:
        res = ""
        for i in address:
            if i==".":
                res += "[.]"
            else:
                res += i
        return res


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return "[.]".join(address.split("."))


class Solution:
    def defangIPaddr(self, address: str) -> str:
        l = address.split(".")
        return "[.]".join(l)
