class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        res = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
                res.append(s[i])
            elif s[i] == ")":
                if stack:
                    stack.pop()
                    res.append(s[i])
            else:
                res.append(s[i])
        while stack:
            x = stack.pop()
            del res[x]
        return "".join(res)

if __name__ == "main":
  test_strings = ["lee(t(c)o)de)", "a)b(c)d", "))(("]
  for s in test_strings:
    res = Solution().minRemoveToMakeValid(s)
    print(res)
