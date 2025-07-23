from typing import Set, List

def distinct(text: str) -> Set[str]:
    return set((c for c in text.upper()))

def sorted_padding(entries: Set[str], padding: int) -> List[str]:
    output = set()
    for entry in entries:
        padded_entry = entry.ljust(padding, ' ')
        output.add(padded_entry.strip())
    return sorted(output)


def combinations(entries: List[str], length: int) -> List[str]:
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


def solve(text: str) -> str:
    combinations_set = set()
    length = len(text)

    for i in range(1, len(text) + 1):
        disctints = combinations(sorted(distinct(text)), i)
        for comb in disctints:
            if comb not in combinations_set:
                combinations_set.add(comb)

    return ' '.join(sorted_padding(combinations_set, length))

n_entries = int(input())

for _ in range(n_entries):
    print(solve(input()))
