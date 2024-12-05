class Vertex:
    def __init__(self, label:int):
        self.label = label
        self.successors = [] # Type Vertex List
        self.predecessors = [] # Type Vertex List

    def addEdge(self, pointsTo:'Vertex'):
        self.successors.append(pointsTo)
        pointsTo.predecessors.append(self)
    
    def addEdges(self, arrPointsTo): # Type Vertex List
        for vertex in arrPointsTo:
            self.addEdge(self, vertex)

    def delEdge(self, pointsTo:'Vertex'):
        self.successors.remove(pointsTo)
        pointsTo.predecessors.remove(self)

    
    def delEdges(self, arrPointsTo): # Type Vertex List
        for vertex in arrPointsTo[:]:
            self.delEdge(vertex)

    def nuke(self):
        self.delEdges(self.successors)

class Graph():
    def __init__(self):
        self.vertices = [] #Type Vertex

    def addVertex(self, vertex:Vertex):
        self.vertices.append(vertex)
    
    def delVertex(self, vertex:Vertex):
        vertex.nuke()
        self.vertices.remove(vertex)

    def findVertex(self, label:int):
        vertices_sorted = radixsort_msb(self.vertices)
        index = binarySearch(vertices_sorted, label)
        return index



def radixsort_msb(arr, k=0):
    if k>31: return arr
    bucket0 = []
    bucket1 = []
    for i in range(0, len(arr)):
        nth_bit = ((arr[i].label) >> k) & 1
        if nth_bit == 0:
            bucket0.append(arr[i])
        else:
            bucket1.append(arr[i])

    return radixsort_msb(bucket0 + bucket1, k+1)


def binarySearch(arr, target):
    left, right = 0, len(arr) - 1  # Initial search bounds
    
    while left <= right:
        mid = left + (right - left) // 2  # Find the middle index
        
        if arr[mid].label == target:
            return mid  # Target found, return the index
        elif arr[mid].label < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half
            
    return -1  # Target not found




def graph_add_order_rules(graph, file="input"):
    with open(file, "r") as f:
            rules = []
            for l in f:
                if l == "\n" or not "|" in l: break
                pre = ""
                succ = ""
                phase = 1
                for c in l:
                    if c.isdigit():
                        if phase == 1: pre+=c
                        else: succ+=c
                    if "|" in c:
                        phase = 2
                
                index = graph.findVertex(int(pre))
                pointsTo = graph.findVertex(int(succ))
                graph.vertices[index].addEdge(graph.vertices[pointsTo])
                

# retuns update array
def get_updates(filename="input"):
    with open(filename, "r") as f:
        updates = []
        for l in f:
            if l == "\n" or len(l) == 5 or "|" in l: continue
            update = []
            temp = ""
            for c in l:
                if c.isdigit():
                    temp+=c
                elif "," in c:
                    update.append(int(temp))
                    temp = ""
            update.append(int(temp))
            updates.append(update)

    return updates
                


def main():
    good_updates = [] # array of all allowed updates
    bad_updates = [] # array of all forbidden updates
    updates = get_updates() # array

    current_line = 1178
    
    for update in updates:
        current_line += 1
        # fail = it exists a broken rule in this update
        fail = False

        # construct graph
        V = Graph()
        for i in range(0,100): # Pages are only 1-99
            vertex = Vertex(i)
            V.addVertex(vertex)
        graph_add_order_rules(V)

        # delete unmentioned pages 
        for vertex in V.vertices[:]:

            if vertex.label in update: pass
            else: V.delVertex(vertex)
        # check for predecessors
        for page in update:
            index = V.findVertex(page)
            if len(V.vertices[index].predecessors) == 0:
                V.delVertex(V.vertices[index])
            else: 
                fail = True
                break

                
        if not fail: 
            good_updates.append(update)
        else: 
            bad_updates.append(update)


    # add up middle array values
    sum = 0
    for update_line in good_updates:
       sum += update_line[len(update_line) // 2]

    print("Done!")
    print(sum)
    #### Part 2 
    # array of bad_updates got already collected above

    fixed_updates = []

    for update in bad_updates[:]:
        # construct graph
        V = Graph()
        for i in range(0,100): # Pages are only 1-99
            vertex = Vertex(i)
            V.addVertex(vertex)
        graph_add_order_rules(V)

        # delete unmentioned pages 
        for vertex in V.vertices[:]:

            if vertex.label in update: pass
            else: V.delVertex(vertex)

        # find vertex with no predecessors
        start = None
        fixed_update = []
        i = 0
        while len(V.vertices) != 0:
            current_label = update[i]
            current_index = V.findVertex(current_label)
            current_vertex = V.vertices[current_index]
            if len(current_vertex.predecessors) == 0:
                fixed_update.append(current_label)
                i=0
                update.remove(current_label)
                V.delVertex(current_vertex)
            else:
                i+=1
            if len(update) == 0: break
            i = i % len(update)


        fixed_updates.append(fixed_update)
    # add up middle array values
    sum = 0
    for update_line in fixed_updates:
        sum += update_line[len(update_line) // 2]    print("Done!")
    print(sum)






        

        





if __name__ == "__main__":
    main()





# For each page to be printed:
# Create a directed graph of requirements.
# Page A must Print before B => A points to B.
# Delete all unrelated nodes.
# a) If an arrow points to X, printing is prohibited.
# b) Otherwise, delete X and all associated arrows.

