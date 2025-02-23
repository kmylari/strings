def minRemoveToMakeValid(s: str) -> str:
    stack = []
    res = []
    for c in s:
        if c == "(":
            res.append(c)
            stack.append(len(res)-1)
        elif c == ")":
            if stack:
                stack.pop()
                res.append(c)
        else:
            res.append(c)
    while stack:
        x = stack.pop()
        del res[x]
    return "".join(res)

if __name__ == '__main__':
  test_strings = ["lee(t(c)o)de)", "a)b(c)d", "))(("]
  for s in test_strings:
    res = minRemoveToMakeValid(s)
    print(res)
