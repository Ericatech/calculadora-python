# Solicita os números ao usuário
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Realiza as operações
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2

# Verifica se a divisão é possível (evitando divisão por zero)
if num2 != 0:
    divisao = num1 / num2
else:
    divisao = "Erro: Divisão por zero!"

# Exibe os resultados
print("\nResultados:")
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")