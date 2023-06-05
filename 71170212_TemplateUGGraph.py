class Graph:
    def __init__(self):
        #constructor
        self._data = {}

    def addVertex(self, key):
        #menambah vertex
        if key not in self._data:
            self._data[key] = set()

    def vertex(self): #mencetak seluruh vertex
        print("\nSeluruh Node = ", end = "")
        # tulis kode Anda di bawah sini
        print()
    
    def edge(self): #mencetak seluruh edge
        print("Seluruh Edge = ", end = "")
        # tulis kode Anda di bawah sini
        print()

    def addEdge(self, x, y):
        #menambah edge antara vertex x dan y
        if x in self._data and y in self._data:
            self._data[x].add(y)
            self._data[y].add(x) #hanya digunakan jika graph tidak berarah

    # untuk pembacaan traversing bfs graph
    def bfs(self, node):
        # silahkan tulis kode Anda di bawah ini 
        print("\n")

# silahkan buat graph seperti pada soal
graph = Graph()
# misalnya 
# graph.addVertex('x')
# graph.addVertex('y')
# graph.addVertex('z')
# graph.addVertex('j')
# graph.addVertex('k')

# graph.addEdge('x', 'y')
# graph.addEdge('x','z')
# graph.addEdge('y', 'z')
# graph.addEdge('z', 'j')

# jangan ubah bagian di bawah 
graph.vertex()
graph.edge()
graph.bfs("a")