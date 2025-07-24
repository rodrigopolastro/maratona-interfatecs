# - = 100%, _ = 110%, ~ = 70%, # = 80%, A-Z = estação, 2 - 999 número de casos similares
# segunda linha = T (METROS DO TRILHO), V (velocidade constante 100%), N (número de casos - A B e A C por exemplo)
# terceira, quarta até N linhas é o número de casos a considerar, ou seja, de A até B e de A até C nesse caso abaixo
# A 12 - ~ 7 _ B ~ 4 # C
# 100 72 2
# A B
# A C
# valores com  precisão de tempo menores que segundos (centésimos) devem ser truncados
# ponto importante! d = (v x t), ou t = d / v

from typing import List, Tuple
from enum import Enum
from string import ascii_uppercase
from dataclasses import dataclass

class TokenKey(Enum):
    STATION = 0
    TIMES = 1
    CURVE = 70
    BRIDGE = 80
    LINE = 100
    UNDERGROUND = 110

TokenValue = str | int
Token = Tuple[TokenKey, TokenValue]

@dataclass(frozen=True)
class Rail:
    token: TokenKey
    distance: float
    velocity: float

def tokenize(read: str) -> List[Token]:
    tokens = []
    token_map = {
        '-': TokenKey.LINE,
        '_': TokenKey.UNDERGROUND,
        '~': TokenKey.CURVE,
        '#': TokenKey.BRIDGE
    }

    for item in read.split():
        if item in token_map:
            tokens.append((token_map[item], item))
        elif item.isnumeric():
            tokens.append((TokenKey.TIMES, item))
        elif item.upper() in ascii_uppercase:
            tokens.append((TokenKey.STATION, item))
        else:
            raise ValueError(f"Invalid token: {item} - BOCA isn't a valid software")

    return tokens

def multiplier(tokens: List[Token]):
    i = 0
    while i < len(tokens):
        if tokens[i][0] == TokenKey.TIMES:
            times = int(tokens[i][1])
            next_token = tokens[i + 1]
            for _ in range(times - 1):
                tokens.insert(i + 1, next_token)
            tokens.pop(i)
        i += 1

    return tokens

# TODO: se o boca trolar, melhorar essa parte
def get_track(tokens: List[Token], start: str, end: str):
    track = []
    start_found = False

    for token in tokens:
        if token[0] == TokenKey.STATION:
            if token[1] == start:
                start_found = True
            elif token[1] == end and start_found:
                break
        if start_found and token[0] != TokenKey.STATION:
            track.append(token)

    return track

def fabric_road(track: List[Token], distance: int, velocity: int) -> List[Rail]:
    rails = []

    for token in track:
        if token[0] == TokenKey.STATION or token[0] == TokenKey.TIMES:
            continue


        distance_km = distance

        if token[0] == TokenKey.LINE:
            rails.append(Rail(token[0], distance_km, velocity))
        elif token[0] == TokenKey.CURVE:
            rails.append(Rail(token[0], distance_km, velocity * 0.7))
        elif token[0] == TokenKey.BRIDGE:
            rails.append(Rail(token[0], distance_km, velocity * 0.8))
        elif token[0] == TokenKey.UNDERGROUND:
            rails.append(Rail(token[0], distance_km, velocity * 1.1))

    return rails

def calculate_time_track(rails: List[Rail]) -> float:
    total_time = 0.0
    for rail in rails:
        time = 3600 / rail.velocity * rail.distance
        total_time += time
    return total_time / 1000


# track = get_track(tokens, 'A', 'B')
# rail_segments = fabric_road(track, distance, velocity)

# print(rail_segments)
# print(calculate_time_track(rail_segments))
def format_time(time: float):
    hours = int(time // 60 // 60 % 100)
    minutes = int(time // 60 % 60)
    seconds = int(time % 60)

    return f"{hours:02}h {minutes:02}min {seconds:02}s"

def solution(city=1):
    pathline = input().strip()
    parameters = input().strip()

    distance, velocity, cases = parameters.split()
    distance, velocity, cases = int(distance), int(velocity), int(cases)

    tokenizer = tokenize(pathline)
    tokens = multiplier(tokenizer)

    print(f'Cidade {city}:')

    for _ in range(cases):
        start, end = input().strip().split()
        roads = fabric_road(get_track(tokens, start, end), distance, velocity)
        timer = calculate_time_track(roads)
        print(format_time(timer))

    print()

try:
    i = 1
    while True:
        solution(i)
        i += 1
except:
    pass
