import time

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


num = int(input("Informe um número para calcule do seu fatorial: "))


if num < 0:
    print("Não é possível calcular o fatorial de um número negativo.") 
else:
    medir_tempo(num)
