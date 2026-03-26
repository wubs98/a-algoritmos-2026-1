
def palindromo(arr):
    if len(arr) <= 1:
        return True
    ##condiçao de parada
    else:
        return arr[0] == arr[-1] and palindromo(arr[1:-1])
    ##verifica recursivamente se o vetor é palindromo
vetor = []

while True:
    item = input("Digite um item para a lista (ou 'sair' para encerrar): ")
    if item.lower() == 'sair':
        break
    vetor.append(item)

print(palindromo(vetor))