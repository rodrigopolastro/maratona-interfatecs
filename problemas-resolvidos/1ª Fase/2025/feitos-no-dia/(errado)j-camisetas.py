# import decimal

# nt = int(input())
# a = tuple(input().split())
# b = tuple(input().split())
# c = tuple(input().split())

# al = (decimal.Decimal(int(a[1])/int(a[0])),int(a[0]),int(a[1]))
# bl = (decimal.Decimal(int(b[1])/int(b[0])),int(b[0]),int(b[1]))
# cl = (decimal.Decimal(int(c[1])/int(c[0])),int(c[0]),int(c[1]))

# lf = sorted([al,bl,cl], key= lambda x : (-x[0],x[1]))

# lfa1 = [lf[0],lf[1],lf[2]]
# lfa2 = [lf[0],lf[2],lf[1]]
# lfb1 = [lf[1],lf[0],lf[2]]
# lfb2 = [lf[1],lf[2],lf[0]]
# lfc1 = [lf[2],lf[0],lf[1]]
# lfc2 = [lf[2],lf[1],lf[0]]

# nt1 = nt
# nt2 = nt
# nt3 = nt
# nt4 = nt
# nt5 = nt
# nt6 = nt
# resp1 = 0
# resp2 = 0
# resp3 = 0
# resp4 = 0
# resp5 = 0
# resp6 = 0

# for valor,qtd,preco in lfa1:
#     rem = nt1//qtd
#     resp1 += preco * rem
#     nt1 -= qtd * rem
# for valor,qtd,preco in lfa2:
#     rem = nt2//qtd
#     resp2 += preco * rem
#     nt2 -= qtd * rem
# for valor,qtd,preco in lfb1:
#     rem = nt3//qtd
#     resp3 += preco * rem
#     nt3 -= qtd * rem
# for valor,qtd,preco in lfb2:
#     rem = nt4//qtd
#     resp4 += preco * rem
#     nt4 -= qtd * rem
# for valor,qtd,preco in lfc1:
#     rem = nt5//qtd
#     resp5 += preco * rem
#     nt5 -= qtd * rem
# for valor,qtd,preco in lfc2:
#     rem = nt6//qtd
#     resp6 += preco * rem
#     nt6 -= qtd * rem
# # print(resp1,resp2,resp3,resp4,resp5,resp6)
# print(max(resp1,resp2,resp3,resp4,resp5,resp6))

# # tecido = int(input())

# # entradas = []

# # for i in range(3):
# #     entrada = map(int, input().split())
# #     entradas.append(entrada)

# # valores = []

# # for custo,lucro in entradas:
# #     total = (tecido // custo) * lucro * custo
# #     valores.append(total)

# # print(max(valores))


ts = int(input())
entradas = []

for i in range(3):
    e = map(int, input().split())
    entradas.append(e)

a = []
for k, v in entradas:
    lt = v / k
    qt = ts // k
    l = v
    a.append((lt, qt, l, k))

a = sorted(a, key=lambda x: (x[0], x[1], x[2]), reverse=True)

din = 0
rem = ts

for lt, qt, l, k in a:
    while rem >= qt:
        din += lt
        
        rem -= k

print(a)

print(int(din))