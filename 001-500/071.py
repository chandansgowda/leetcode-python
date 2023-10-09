class Solution:
    def simplifyPath(self, path: str) -> str:
        dirOrFiles = []
        path = path.split("/")
        for x in path:
            if dirOrFiles and x=="..":
                dirOrFiles.pop()
            elif x not in [".","..",""]:
                dirOrFiles.append(x)

        return "/"+"/".join(dirOrFiles)
