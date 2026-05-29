import sys

class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        # Inicializa a matriz de adjacência com zeros
        self.grafo = [[0 for _ in range(vertices)] for _ in range(vertices)]
        # Dicionário para mapear índices para os nomes das cidades
        self.cidades = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'}

    def imprimir_mst(self, pai):
        print("Conexões de Fibra Óptica (Árvore Geradora Mínima):")
        print("-------------------------------------------------")
        custo_total = 0
        for i in range(1, self.V):
            origem = self.cidades[pai[i]]
            destino = self.cidades[i]
            peso = self.grafo[i][pai[i]]
            print(f"Polo {origem} <--> Polo {destino} \tCusto: {peso} km")
            custo_total += peso
        
        print("-------------------------------------------------")
        print(f"Total de fibra óptica necessária: {custo_total} km")

    def chave_minima(self, chave, mst_set):
        minimo = sys.maxsize
        indice_minimo = -1

        for v in range(self.V):
            if chave[v] < minimo and mst_set[v] == False:
                minimo = chave[v]
                indice_minimo = v

        return indice_minimo

    def algoritmo_prim(self):
        # Array para armazenar a árvore geradora mínima
        pai = [None] * self.V
        # Valores chave usados para escolher o peso mínimo da aresta
        chave = [sys.maxsize] * self.V
        # Para rastrear os vértices já incluídos na MST
        mst_set = [False] * self.V

        # Sempre começamos do primeiro vértice (Polo A)
        chave[0] = 0
        pai[0] = -1 

        for _ in range(self.V):
            # Escolhe o vértice com a distância mínima do conjunto de vértices não processados
            u = self.chave_minima(chave, mst_set)
            
            # Coloca o vértice escolhido no conjunto da MST
            mst_set[u] = True

            # Atualiza os valores chave e os pais dos vértices adjacentes ao vértice escolhido
            for v in range(self.V):
                # self.grafo[u][v] > 0 verifica se há conexão
                # mst_set[v] == False verifica se v já está na MST
                # chave[v] > self.grafo[u][v] verifica se o novo caminho é menor
                if self.grafo[u][v] > 0 and mst_set[v] == False and chave[v] > self.grafo[u][v]:
                    chave[v] = self.grafo[u][v]
                    pai[v] = u

        self.imprimir_mst(pai)

# Execução do Exercício
if __name__ == '__main__':
    # 6 Polos (A=0, B=1, C=2, D=3, E=4, F=5)
    g = Grafo(6)
    
    # Preenchendo a matriz de adjacência com base na tabela do exercício
    g.grafo = [
        [0, 4, 4, 0, 0, 0], # A
        [4, 0, 2, 5, 0, 0], # B
        [4, 2, 0, 5, 6, 0], # C
        [0, 5, 5, 0, 3, 4], # D
        [0, 0, 6, 3, 0, 2], # E
        [0, 0, 0, 4, 2, 0]  # F
    ]

    g.algoritmo_prim()