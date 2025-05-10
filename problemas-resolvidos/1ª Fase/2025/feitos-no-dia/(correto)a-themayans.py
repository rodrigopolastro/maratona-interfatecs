def calc_token(token: str):
    if token == "*":
        return 0
    return token.count(".") + token.count("-") * 5

result = -1
while result != 0:
    tokens = input().split()
    s, m = 0, 0
    for i in range(len(tokens) - 1, -1, -1):
        t = tokens[i]
        s += (calc_token(t) * (20 ** m))
        m += 1
    result = s
    print(result)


