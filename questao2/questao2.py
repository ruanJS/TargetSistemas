def is_fibonacci(num):
    if num < 0:
        return False

    a, b = 0, 1
    while a < num:
        a, b = b, a + b

    return a == num


# Número de entrada
numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

if is_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
