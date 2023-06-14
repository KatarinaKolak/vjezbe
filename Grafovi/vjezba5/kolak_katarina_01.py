def setEdgeIdentifier(nodes, edge):
    for node in nodes:
        if edge == node[0]:
            return node[1]

def setGraph(nodes, edges): # postavlja se dictionary koristeci vrhove i bridove 
    graph = {}
    for node in nodes:
        lst = [(setEdgeIdentifier(nodes, edge[1]), edge[2]) for edge in edges if node[0] == edge[0]]
        vartex = node[1]
        graph[vartex] = lst
    return graph

def readPajek(myFile):
    file = open(myFile,'r')
    nodes = []
    edges = []
    lst = [line.strip() for line in file.readlines()] # spremimo sve iz filea u listu 
    for node in range(len(lst)-1):
        if "*Vertices" in lst[node]:  # dohvacaju se vrhovi
            nodes = [(lst[i][0], lst[i][3:4]) for i in range (node+1, int(lst[node][-1])+1)]
        elif lst[node].startswith('*'):  # dohvacaju se bridovi
            tempEdges = [(lst[i][0], lst[i][2], "e" + str(i)) for i in range (node+1, len(lst)-1)]
            if tempEdges != 0:
                edges = tempEdges
    return setGraph(nodes, edges)
   
def checkNode(node, values): # provjera nalazi li se vrh medu bridovima 
    for value in values:
        if node in value[0]:
            return True
    return False

def convertToNeighbourMatrix(graph):
    matrix = []
    nodes = graph.keys()
    for value in graph.values():
        neighbours = [1 if checkNode(node, value) else 0 for node in nodes] # ako se nalazi medu bridovima onda spada 2 vrha
        matrix.append(neighbours)
    return matrix

def convertToIncidenceMatrix(graph):
    matrix = []
    edges = [edge for element in graph.values() for edge in element] # bridovi 
    for key, value in graph.items():
        incidence = []
        for edge in edges:
            if key == edge[0]: # ako je medu kljucevima radi se o dolaznom bridu
                incidence.append(-1)
            elif edge in value:  # ako je medu vrijednostima onda je odlazni brid
                incidence.append(1)
            else:
                incidence.append(0) # ni dolazni ni odlazni 
        matrix.append(incidence)
    return matrix

def countNodes(graph):
    return len(graph.keys())

def countEdges(graph):
    edges = [edge[0] for element in graph.values() for edge in element]
    return len(edges)

def countDegree(matrix):
    edgeSum = {}
    for element in range(len(matrix)):
        edgeSum[element+1] = (sum(matrix[element]))  # sumira redak u matrici i spremi u dictionary
        
    return edgeSum
        
def maxIncidenteEdge(matrix):
    edgeSum = countDegree(matrix)
    
    maxSum = max(edgeSum.values())
    maxSumNodes = [key for key, values in edgeSum.items() if maxSum == values] # spremi u listu u slucaju da ima vise istih max vrijednosti
    return maxSumNodes

def eulerGraph(matrix):
    degree = countDegree(matrix)
    for value in degree.values():
        if value % 2 != 0:
            return False
    return True

def checkOddDegree(matrix):
    degreeLst = countDegree(matrix)
    count = 0
    for key, values in degreeLst.items():
        if values % 2 != 0 and values != 0:
            count += 1
            
    return count

def dfs(graph, node, visited=[]):
    visited.append(node)
        
    for neighbour in graph[node]:
        if neighbour[0] not in visited:
            dfs(graph, neighbour[0], visited)
            
    return visited

def isConnected(graph):
    visited = dfs(graph, list(graph.keys())[0])
    for key in graph.keys():
        if key not in visited:
            return False
    return True

def findOddDegreeNode(graph):
    degreeLst = countDegree(convertToNeighbourMatrix(graph))
    
    for key, values in degreeLst.items():
        if values % 2 != 0:
            return key

def isOddDegree(graph):
    if checkOddDegree(convertToNeighbourMatrix(graph)) == 0 or checkOddDegree(convertToNeighbourMatrix(graph)) == 2:
        return True
    return False

def isPath(graph):
    if isConnected(graph) and isOddDegree(graph):
        print("DA")
        return True
    return False
    
def hierholzerAlgorithm(graph):
    '''if not isPath(graph):
        return False'''
    
    stack = []
    path = []
    visited = []
    stack.append(list(graph.keys())[0])
    
   # if checkOddDegree(convertToNeighbourMatrix(graph)) == 2:
    #    stack.append(str(findOddDegreeNode(graph)))
    #elif checkOddDegree(convertToNeighbourMatrix(graph)) == 0:
     #   stack.append(list(graph.keys())[0])
    nextNode = ""
    while stack:# dok ima vrhova na stacku
        currentVisited = stack[-1] # uzmi vrh sa stacka
        
        if len(graph[currentVisited]) > 0 and graph[currentVisited][-1] not in visited: # ako nisu svi posjeceni jos
            nextNode = graph[currentVisited].pop()  
            stack.append(nextNode[0]) # stavi drugi kraj na stack
            visited.append(nextNode) # oznaci brid kao posjeceni
        else: 
            path.append((stack.pop())) # digni vrh sa stacka i dodaj ga u put 
        
        
    path.reverse() #ispisemo u obrnutom redosljedu
    return path
        
def main():
    file = 'euler.net'
    graph = readPajek(file)
    print(graph)
    
    
    matrix = convertToNeighbourMatrix(graph)
    print(matrix)
    print("Degree: ", countDegree(matrix))
    print(checkOddDegree(matrix))
    '''
    incidence = convertToIncidenceMatrix(graph)
    #print(incidence)
    print("Nodes num: ", countNodes(graph))
    print("Edges num: ", countEdges(graph))
    print("Degree: ", countDegree(matrix))
    print("Max incidente edge: ", maxIncidenteEdge(matrix))
    print("Is euler: ", eulerGraph(matrix))
    print("DFS: ", dfs(graph, '1'))
    print("Euler path:", hierholzerAlgorithm(graph))
    matrix = convertToNeighbourMatrix(graph)
    print(matrix)
    print("Degree: ", countDegree(matrix))
    #print ("DFS: ", leafy.search.DFS(graph2, '1'))
    #print(isConnected(graph))
    #print("Odd degrees: ", checkOddDegree(matrix))
    print()'''
    print("Euler path:", hierholzerAlgorithm(graph))

if __name__=='__main__':
    main()