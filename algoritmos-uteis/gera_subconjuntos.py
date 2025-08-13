# gera subconjuntos de combinações de caracteres.
# ExemploS:
# - combinations('ABC', 1) -> [A, B, C]
# - combinations('WXYZ', 2) -> [WX, WY, WZ ... YZ]
def combinations(entries, length):
    if length == 0:
        return ['']

    if len(entries) == 0:
        return []

    entries = sorted(entries)
    result = []

    for i in range(len(entries)):
        current = entries[i]
        remaining = entries[i + 1:]
        for comb in combinations(remaining, length - 1):
            result.append(current + comb)

    return result

