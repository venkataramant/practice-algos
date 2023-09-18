class Solution:

    def isValid(self, s: str) -> bool:
        openList = list()
        for ch in s:
            if ch in ("{", "[", "("):
                openList.append(ch)
            else:
                if len(openList) > 0:
                    lob = openList.pop()
                    if (ch == "}" and lob == "{") or (ch == "]" and lob == "[") or (ch == ")" and lob == "("):
                        continue
                    else:
                        return False
                else:
                    return False
        return True if len(openList) == 0 else False


if __name__ == "__main__":
    sol = Solution()
    inputs = ("()", "()[]{}", "(]")
    for s in inputs:
        print(" isValid -->", sol.isValid(s), s)

