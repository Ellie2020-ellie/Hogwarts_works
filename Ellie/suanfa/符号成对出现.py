def isBracketPair(a):
    bracketAll = {")": "(", "]": "[", "}": "{"}
    b = []
    for i in a:
        if i in bracketAll.values():
            b.append(i)
        elif len(b) > 0 and b[-1] == bracketAll.get(i):
            b.pop()
        else:
            return "bad"
    if len(b) == 0:
        return "ok"
    else:
        return "bad"


if __name__ == '__main__':
    x = isBracketPair(["]", "(", ")", "]", "{"])
    print(x)
