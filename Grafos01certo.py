class Grafo:
    def __init__(self, vertice):
        self.v = vertice
        self.adjacentMatriz = [[0 for i in range(self.v)] for j in range(self.v)]

    def AddEdges(self, src, dest, custo):
        if src == dest:
            print("Mesma origem e destino")
        else:
            self.adjacentMatriz[src][dest] = custo
            self.adjacentMatriz[dest][src] = custo

    def GetNeighbours(self, src):
        lst = []
        for i in range(len(self.adjacentMatriz[src])):
            if self.adjacentMatriz[src][i] > 0:
                lst.append(i)
        return lst
    
    def DijkstraShortestPath(self,src,dest):
        dct = {}
        for i in range(len(self.adjacentMatriz)):
            temp = {}
            x = self.GetNeighbours(i)
            for j in x:
                temp[j] = self.adjacentMatriz[i][j]
            dct[i] = temp
        
        inicio = src
        fim = dest
        menor_dist = {}
        pred = {}
        nos_nao_vistos = dct
        infinito = 9999999
        path = []
        maiores = 0
        for node in nos_nao_vistos:
            menor_dist[node] = infinito
        menor_dist[inicio] = 0

        while nos_nao_vistos:
            minNode = None
            for node in nos_nao_vistos:
                if minNode is None:
                    minNode = node
                elif menor_dist[node] < menor_dist[minNode]:
                    minNode = node

            for filho, peso in dct[minNode].items():
                if peso + menor_dist[minNode] < menor_dist[filho]:
                    menor_dist[filho] = peso + menor_dist[minNode]
                    pred[filho] = minNode
            nos_nao_vistos.pop(minNode)

        no_atual = fim
        while no_atual != inicio:
            try:
                path.insert(0,no_atual+1)
                no_atual = pred[no_atual]
            except KeyError:
                print('Caminho nao alcançável')
                break
        path.insert(0,inicio+1)
        if menor_dist[fim] != infinito:
            maiores += menor_dist[fim]
            print('Menor distancia é', str(menor_dist[fim]))
            print('E o caminho é', str(path))
            print('\n')
            return maiores
        

g = Grafo(12)
g.AddEdges(0,1,17)
g.AddEdges(0,2,25)
g.AddEdges(0,4,21)
g.AddEdges(1,3,10)
g.AddEdges(1,5,15)
g.AddEdges(2,6,20)
g.AddEdges(3,5,9)
g.AddEdges(3,7,23)
g.AddEdges(4,5,12)
g.AddEdges(4,6,19)
g.AddEdges(5,7,8)
g.AddEdges(5,8,7)
g.AddEdges(6,8,17)
g.AddEdges(6,10,12)
g.AddEdges(6,11,22)
g.AddEdges(7,8,10)
g.AddEdges(7,9,13)
g.AddEdges(8,9,12)
g.AddEdges(8,10,15)
g.AddEdges(9,10,14)
g.AddEdges(9,11,21)
g.AddEdges(10,11,10)

list_maiores = []

for i in range(12):
    maiores2=0
    for j in range(12):
        print('DO GRAFO', i+1,'AO GRAFO', j+1)
        maiores = g.DijkstraShortestPath(i,j)
        maiores2 += maiores
    list_maiores.append(maiores2)
    print('---------------------------------------')

print('lista de distancias totais', list_maiores)
index = list_maiores.index(min(list_maiores))
print('O elemento central é:',index+1)