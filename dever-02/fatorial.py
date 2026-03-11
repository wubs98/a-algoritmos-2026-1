import time
import sys

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

def medir_tempo(p):
    inicio = time.perf_counter()
    resultado = fatorial(p)
    fim = time.perf_counter()
    tempo = fim - inicio
    print(f"O fatorial de {num} é {resultado}")
    print(f"Tempo de Execução: {tempo:.10f} segundos")
    operacao = str(input("Para calcular outro número, pressione qualquer tecla. Pressione N para encerrar: "))
    if operacao == "n":
        sys.exit()
    elif operacao == "N":
        sys.exit()
    

x = 0


while x%2 == 0:
    num = int(input("Informe um número para o calculo do seu fatorial: "))
    if num < 0:
        print("Não é possível calcular o fatorial de um número negativo.") 
    else:
        medir_tempo(num)
    x = x/2
