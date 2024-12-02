def gcd(a, b):
    while b != 0:
        a, b = b, a % b  # Algoritmo de Euclides
    return a

# Teste da função
resultado = gcd(24, 33)
print(f"MDC = {resultado}")