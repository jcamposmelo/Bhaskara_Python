import math

# Entrada de dados - coeficientes a, b e c
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

# Cálculo do discriminante
delta = b**2 - 4*a*c

# Verificação das raízes (raízes reais, raízes iguais, raízes complexas)
if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("As raízes são", x1, "e", x2)
elif delta == 0:
    x = -b / (2*a)
    print("A raiz é", x)
else:
    parte_real = -b / (2*a)
    parte_imaginaria = math.sqrt(-delta) / (2*a)
    print("As raízes são complexas: {} + {}i e {} - {}i".format(parte_real, parte_imaginaria, parte_real, parte_imaginaria))
