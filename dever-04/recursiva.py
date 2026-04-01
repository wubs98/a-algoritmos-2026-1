def recorrencia(n):
    if (n == 1):
        return 2

    return 2 * recorrencia(n - 1) + n**2

def main():
    n = int(input("Digite um número inteiro: "))
    resultado = recorrencia(n)
    print(f"O resultado da recorrência para n={n} é: {resultado}")

main();
