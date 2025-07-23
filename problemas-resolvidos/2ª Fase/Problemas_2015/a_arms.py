from typing import Tuple

def arms(n: int) -> Tuple[int, int]:
    nums = [int(i) for i in str(n)]
    digits = len(nums)
    return (sum((n ** digits for n in nums)), digits)

while True:
    read = int(input())

    if not read:
        break

    output, digits = arms(read)
    if output == read:
        print(digits)
        continue

    print("N")
