from typing import Tuple

def binary(n: int) -> str:
    return bin(n)[2:].rjust(8, '0')

def ip(read: str) -> str:
    blocks = read.split('.')
    output = ''.join((binary(int(n)) for n in blocks))
    return output

def read(text: str) -> Tuple[str, str, str]:
    ip1, ip2, mask = text.split(' ')
    return (ip1, ip2, mask)

def solve(ip1: str, ip2: str, mask: str) -> str:
    for i in range(len(mask)):
        bitmask = mask[i]
        if bitmask != '1':
            break
        ip1_bit = ip1[i]
        ip2_bit = ip2[i]
        if ip1_bit != ip2_bit:
            return 'N'
    return 'S'

try:
    while True:
        ip1, ip2, mask = read(input())
        print(solve(ip(ip1), ip(ip2), ip(mask)))
except:
    pass
