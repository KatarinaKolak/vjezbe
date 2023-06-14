import csv
import numpy
from itertools import permutations
import time

def read_csv(file):
    with open(file) as f:
        reader = csv.reader(f, delimiter = ',')
        edges = list(reader)  # bridovi
        matrix = numpy.array(edges)
    return matrix
    
    
def read_city(file): # citanje gradova koje se zeli obici
    lst_city = []
    with open(file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            lst_city.append(''.join(row))
        
    return lst_city

def to_graph(matrix, cities):
    graph = {}
    nodes = matrix[0][1:]  #dohvacamo vrhove, preskoci se ',' 
    matrix = matrix[1:] # definiramo bridove preskoci se prvi redak matrice 
    neighbour = []
    city = 0
    n_index = 0
    for node in range(len(nodes)):
        neighbours = [element for element in range(len(cities)) if element != city]
        for edge in range(len(matrix)):
            if matrix[edge][0] != nodes[node] and nodes[node] in cities and matrix[edge][0] in cities and matrix[node][edge+1].isnumeric():  # ako se radi o susjedima vrha node
                neighbour.append((neighbours[n_index],int(matrix[node][edge+1])))
                n_index += 1 # da kljucevi budu po redu zbog permutacija
        if len(neighbour) > 0: # ako je grad kojeg se zeli obici
            graph[city] = neighbour
            neighbour = []
            city += 1 # da kljucevi budu po redu zbog permutacija
            n_index = 0
    return graph

    
def findPath(all_paths, min_distance): # iz svih ciklusa izaberemo najmanji
    for distance, path in all_paths.items():
        if distance == min_distance:
            return path
        
def brute_force(matrix):
    perms = list(permutations(range(len(matrix)), len(matrix)))  #generiranje permutacija 
    distance_list = []
    path = {}
    lst = []
    distance = 0
    
    for perm in perms:
        for element in range(len(perm)):
            if element < len(perm)-1:
                distance += int(matrix[perm[element]][perm[element+1]]) #zbrajanje elemenata matrice ovisno o indeksu
                lst.append(matrix[perm[element]][perm[element+1]])
            else:
                distance += int(matrix[perm[element]][perm[0]])
                lst.append(matrix[perm[element]][perm[0]])
                
        distance_list.append(distance)
        path[distance] = lst #  sacuvamo path da ga mozemo vratiti 
        distance = 0
        lst = []
        
    final_path = findPath(path, min(distance_list))
    return min(distance_list, key = int), final_path
          
def min_neighbour(path): # trazi susjeda sa najmanjom tezinom
    values = [int(value) for value in path.values()] #lista susjeda 
    #values = values.astype(numpy.int)
    
    min_element = min(values) #susjed najmanje tezine
    for key, value in path.items():
        if int(value) == min_element:
            return key, min_element #vratimo vrh i brid onog brida najmanje tezine

def unvisited_neighbours(neighbours, visited): # trazi neposjecene 
    unvisited = {}
    
    for neighbour in neighbours:
        if int(neighbour[0]) not in visited: # ako nije u visited dodaj ga
            unvisited[neighbour[0]] = neighbour[1]
        
    return min_neighbour(unvisited) #vrati najmanji trenutni neposjeceni

def nearest_neighbour(start, graph):
    visited = [] #lista posjecenih gradova
    
    visited.append(int(start)) #dodamo pocetni grad u matricu
    currentCity = -1 #trenutno posjeceni grad
    sum_distance = 0 
    
    while len(visited) < len(graph.keys()): #dok se ne posjete svi gradovi
        currentCity = visited[-1] #uzima se zadnji dodan u visited
        node, distance = unvisited_neighbours(graph[currentCity], visited) #traze se njegovi neposjeceni susjedi
        visited.append(node) # spremimo vrh u posjecene 
        sum_distance += distance #dodamo udaljenost u sumu
        
    sum_distance += graph[visited[-1]][start][1] # dodati i tezinu pocetnog zbog vracanja u njega    
    return visited, sum_distance

def neighbour_list(graph):
    lst = []
    for key, values in graph.items():
        for value in values:
            lst.append((key, *value))
    return lst

def dfs(graph, node, visited=[]):
    visited.append(node)
        
    if node in graph.keys():
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

def checkNode(node, values): # provjera nalazi li se vrh medu bridovima 
    for value in values:
        if node in value:
            return True
    return False

def convertToNeighbourMatrix(graph):
    matrix = []
    nodes = graph.keys()
    for value in graph.values():
        neighbours = [1 if checkNode(node, value) else 0 for node in nodes] # ako se nalazi medu bridovima onda spada 2 vrha
        matrix.append(neighbours)
    return matrix

def countDegree(matrix):
    edgeSum = {}
    for element in range(len(matrix)):
        edgeSum[element+1] = (sum(matrix[element]))  # sumira redak u matrici i spremi u dictionary
        
    return edgeSum

def checkOddDegree(matrix):
    degreeLst = countDegree(matrix)
    count = 0
    for key, values in degreeLst.items():
        if values % 2 != 0 and values != 0:
            count += 1
            
    return count

def isThirdDegree(graph):
    if checkOddDegree(convertToNeighbourMatrix(graph)) == 3:
        return True
    return False
        
def isCycle(graph, start):
    visited = dfs(graph, start)
    
    if visited[-1] in graph.keys():
        for element in graph[visited[-1]]:
            if element[0] == start: #ako se moze vratiti na pocetak
                return True
    return False
    
    
def sorted_edges(graph):
    new_graph = {}
    sorted_edge = neighbour_list(graph)
    sorted_edge.sort(key = lambda x : x[2]) # sortiramo po trecem elementu
    distance = 0
    visited = []
    
    while len(visited) < len(graph.keys()):
        min_element = min(sorted_edge, key = lambda x : x[2])
            
        if min_element[0] in visited:
            sorted_edge.remove(min_element)
        
        else:
            new_graph[min_element[0]] = [(min_element[1], min_element[2])]
            if isCycle(new_graph, min_element[0]) or isThirdDegree(new_graph):
                sorted_edge.remove(min_element)
                new_graph.popitem()
            else:
                distance += min_element[2]
                visited.append(min_element[0])
                sorted_edge.remove(min_element)
        
    return distance, new_graph
    
def sort_graph(graph): # sa sortiranje liste grafova 
    ngraph = {}
    for k, values in graph.items():
        ngraph[k] = sorted(values, key=lambda x: x[0])
    return ngraph

def to_neighbour_matrix(graph):
    matrix = []
    lst = [values.append((key, 0)) for key, values in graph.items()] # ubaciti i vlastiti vrh u listu susjedstva
    
    sorted_graph = sort_graph(graph) # sortirati liste 

    for key, values in sorted_graph.items(): # generirati matricu iz grafa
        lst = [0 if key == values[value][0] else values[value][1] for value in range(len(values))]
        matrix.append(lst)
    return matrix 

def main():
    matrix = read_csv('distance.csv')
    cities = read_city('gradovi.txt')
    graph = to_graph(matrix, cities)
    neighbour_matrix = to_neighbour_matrix(graph)
    #print(neighbour_matrix)
    t0 = time.process_time()
    distance, path = brute_force(neighbour_matrix)
    t1 = time.process_time()
    print("Ciklus najmanje tezine je:", distance, "vrijeme izvodenja:", t1 - t0)
    
    t2 = time.process_time()
    path2, distance2 = nearest_neighbour(0, graph)
    t3 = time.process_time()
    print("Ciklus najmanje tezine je:", distance2, "vrijeme izvodenja:", t2 - t3)
    
    t4 = time.process_time()
    distance3, path3 = sorted_edges(to_graph(matrix, cities))
    t5 = time.process_time()
    print("Ciklus najmanje tezine je:", distance3, "vrijeme izvodenja:", t5 - t4)

if __name__=='__main__':
    main()