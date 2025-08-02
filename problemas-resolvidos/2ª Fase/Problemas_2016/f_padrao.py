def solve(read: str):
    if len(read) <= 1:
        return read

    word = read[0]
    groups = {}

    for letter in read[1:]:
        if letter == word[0]:
            groups[word] = read.count(word)

        word += letter

    if len(groups) == 0:
        return [(read, 1)]

    return sorted(groups.items(), key=lambda x: (x[1], len(x[0])), reverse=True)

try:
    while True:
        read = input()
        solution = solve(read)
        print(f"{solution[0][1]} * {solution[0][0]}")
except EOFError:
    pass
