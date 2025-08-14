# 📚 Python 3.10+ — Compilado de Funções Úteis (`math` e `functools`)

## 📐 math

> Biblioteca para operações matemáticas rápidas e precisas. Trabalha com floats e alguns inteiros grandes.

### 🔢 Aritmética e potências

- `math.ceil(x)` → Arredonda para cima.
- `math.floor(x)` → Arredonda para baixo.
- `math.trunc(x)` → Trunca (remove parte decimal).
- `math.fabs(x)` → Valor absoluto como `float`.
- `math.factorial(n)` → Fatorial de `n` (inteiro).
- `math.prod(iterable, *, start=1)` → Produto de todos os elementos.
- `math.isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)` → Compara floats com tolerância.

### 📏 Potência e raízes

- `math.sqrt(x)` → Raiz quadrada.
- `math.pow(x, y)` → Potência (float).
- `math.exp(x)` → e^x.
- `math.log(x, base)` → Logaritmo (base opcional).
- `math.log10(x)` → Log base 10.
- `math.log2(x)` → Log base 2.

### 🎯 Trigonometria

- `math.sin(x)`, `math.cos(x)`, `math.tan(x)` → Funções trigonométricas (x em radianos).
- `math.asin(x)`, `math.acos(x)`, `math.atan(x)` → Inversas.
- `math.atan2(y, x)` → Ângulo entre ponto (x, y) e eixo X.
- `math.radians(graus)` → Converte para radianos.
- `math.degrees(radianos)` → Converte para graus.
- `math.hypot(*coords)` → Distância euclidiana.

#### Extra - Graus <-> Radianos com um valor de pi arbitrário

```python
# Definindo o valor de pi
PI = 3.141592653589793

# Converter graus para radianos
def graus_para_radianos(graus):
    return graus * (PI / 180)

# Converter radianos para graus
def radianos_para_graus(radianos):
    return radianos * (180 / PI)
```

### 📊 Outros utilitários

- `math.comb(n, k)` → Combinações (n choose k).
- `math.perm(n, k)` → Permutações.
- `math.gcd(a, b, *rest)` → Máximo divisor comum.
- `math.lcm(a, b, *rest)` → Mínimo múltiplo comum.
- `math.copysign(mag, sign)` → Copia sinal.
- `math.dist(p, q)` → Distância entre dois pontos (iteráveis).
- `math.fsum(iterable)` → Soma precisa de floats.
- Constantes úteis:  
  `math.pi`, `math.e`, `math.tau`, `math.inf`, `math.nan`.
