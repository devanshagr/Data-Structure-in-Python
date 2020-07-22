import copy
import math
from collections import defaultdict, deque
from heapq import heapify, heappush, heappop, heapreplace, heappushpop

#  from branch master
# one more comment from master
# from branch new-branch
# something in new branch
# adding to master
class Graph(object):

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, src, dest):
        self.graph[src].append(dest)
    
    def add_edge_undirected(self, src, dest):
        self.graph[src].append(dest)
        self.graph[dest].append(src)

    def add_edge_with_weight(self, src, dest, weight):
        self.graph[src].append((dest, weight))
    
    def add_edge_with_weight_undirected(self, src, dest, weight):
        self.graph[src].append((dest, weight))
        self.graph[dest].append((src, weight))

    def bfs_util(self, start, visited, output):
        # visited = [False]*len(self.graph)
        queue = deque()
        queue.append(start)
        visited[start] = True
        
        while queue:
            start = queue.popleft()
            output.append(start)
            print (start)

            for node in self.graph[start]:
                if not visited[node]:
                    queue.append(node)
                    visited[node] = True

    def bfs_disconnected(self, start, output):
        visited = [False]*len(self.graph)
        for node in self.graph:
            if not visited[node]:
                self.bfs_util(node, visited, output)

    def dfs_util(self, start, visited, output):
        visited[start] = True
        # print (start)
        output.append(start)

        for vertex in self.graph[start]:
            if not visited[vertex]:
                self.dfs_util(vertex, visited, output)

    def dfs_disconnected(self, start, output):
        visited = [False]*len(self.graph)
        for vertex in self.graph:
            if not visited[vertex]:
                self.dfs_util(vertex, visited, output)

    def print_all_mother_vertex_basic_method(self):
        for vertex in self.graph:
            output = []
            visited = [False]*len(self.graph)
            self.dfs_util(vertex, visited, output)
            if len(output) == len(self.graph):
                print ('{} is the mother vertex'.format(vertex))

    def mother_vertex_efficient(self):
        visited = [False]*len(self.graph)
        output = []
        for vertex in self.graph:
            if not visited[vertex]:
                self.dfs_util(vertex, visited, output)
                last_vertex = vertex

        visited = [False]*len(self.graph)
        output = []
        self.dfs_util(last_vertex, visited, output)
        if len(output) == len(self.graph):
                print ('{} is the mother vertex'.format(last_vertex))

    def nodes_at_given_level_bfs(self, start, level, output):
        q = deque()
        visited = [False]*len(self.graph)
        q.append(start)
        visited[start] = True
        curr_level = 0
        while q:
            count = len(q)
            curr_level += 1
            while count > 0:
                count -= 1
                start = q.popleft()
                if level == curr_level:
                    output.append(start)

                for vertex in self.graph[start]:
                    if not visited[vertex]:
                        q.append(vertex)
                        visited[vertex] = True

    def find_path_between_2_vertices(self, src, dest, path):
        path.append(src)
        if src == dest:
            return path
        for vertex in self.graph[src]:
            if vertex not in path:
                return self.find_path_between_2_vertices(vertex, dest, path)
    
    def all_possible_paths(self, src, dest, path, output):
        path.append(src)
        if src == dest:
            output.append(copy.deepcopy(path))
        else:
            for vertex in self.graph[src]:
                if vertex not in path:
                    self.all_possible_paths(vertex, dest, path, output)
        # to backtrack
        path.pop()

    def min_path_between_2_vertex(self, src, dest, path, output):
        path.append(src)
        if src == dest:
            if not output:
                new_path = copy.deepcopy(path)
                output.append(new_path)
            else:
                new_path = copy.deepcopy(path) if len(path) < len(output[0]) else output[0]
                output[0] = new_path
        else:
            for vertex in self.graph[src]:
                if vertex not in path:
                    self.min_path_between_2_vertex(vertex, dest, path, output)
        
        path.pop()

    def min_path_between_2_vertex_bfs(self, src, dest):
        q = deque()
        visited = set()
        found = False
        output = {i:[] for i in self.graph}
        output[src] = [src]
        start = src
        q.append(start)
        visited.add(start)
        while q:
            start = q.popleft()
            for vertex in self.graph[start]:
                if vertex not in visited:
                    q.append(vertex)
                    visited.add(vertex)
                    output[vertex] = output[start] + [vertex]
                if vertex == dest:
                    found = True
            if found:
                break
                    
        return output

    # cycle detection with dfs for directed and with bfs for undirected (easy)
    def detect_cycle_directed(self):
        visited = set()
        rec_stack = set()
        vertexes = list(self.graph.keys())

        def detect_cycle_util(start, visited, rec_stack):
            visited.add(start)
            rec_stack.add(start)

            for vertex in self.graph[start]:
                if vertex not in visited:
                    if detect_cycle_util(vertex, visited, rec_stack):
                        return True
                elif vertex in rec_stack:
                    return True

            rec_stack.remove(start)
            return False
        
        for vertex in vertexes:
            if vertex not in visited:
                if detect_cycle_util(vertex, visited, rec_stack):
                    return True
                
        return False

    def detect_cycle_undirected_dfs(self):
        visited = set()
        vertexes = list(self.graph.keys())

        def detect_cycle_undirected_dfs_util(start, visited, parent):
            visited.add(start)

            for vertex in self.graph[start]:
                if vertex not in visited:
                    if detect_cycle_undirected_dfs_util(vertex, visited, start):
                        return True
                elif parent != vertex:
                    return True
            
            return False

        for vertex in vertexes:
            if vertex not in visited:
                if detect_cycle_undirected_dfs_util(vertex, visited, -1):
                    return True
        return

    #TODO
    def detect_cycle_undirected_union_find(self):

        vertexes = list(self.graph.keys())
        parent = {i:-1 for i in self.graph}
        def find(parent, vertex):
            if parent[vertex] == -1:
                return vertex
            else:
                return find(parent, parent[vertex])

        def union(parent, x, y):
            parent[x] = y

        
        for vertex in vertexes:
            for child in self.graph[vertex]:
                x = find(parent, vertex)
                y = find(parent, child)
                if x == y:
                    return True
                else:
                    union(parent, x, y)

        return False

    def topological_sort(self):
        temp_stack = []
        visited = set()
        vertexes = list(self.graph.keys())

        def topological_sort_util(start, visited, temp_stack):
            visited.add(start)
            for vertex in self.graph[start]:
                if vertex not in visited:
                    topological_sort_util(vertex, visited, temp_stack)
            
            temp_stack.insert(0, start)

        for start in vertexes:
            if start not in visited:
                topological_sort_util(start, visited, temp_stack)

        return temp_stack

    
    def topological_sort_kahns_indegree(self):
        
        in_degree = {}
        
        # for vertex in self.graph:
        #     in_degree[vertex] = 0
        
        # get indegree
        for vertex in self.graph:
            for neighbour in self.graph[vertex]:
                in_degree[neighbour] = in_degree.get(neighbour, 0) + 1
        
        # queue all vertixes with 0 in degree
        q = deque()
        count = 0
        order = []

        # for vertex, degree in in_degree.items():
        #     if degree == 0:
        #         q.append(vertex)
        
        # more efficient then above commented since we dont have to initialize grapph vertices to be 0
        # [q.append(vertex) for vertex in in_degree if in_degree[vertex] == 0]
        [q.append(vertex) for vertex in self.graph if vertex not in in_degree]
        
        
        while q:
            current = q.popleft()
            order.append(current)

            for neighbour in self.graph[current]:
                in_degree[neighbour] -= 1

                if in_degree[neighbour] == 0:
                    q.append(neighbour)
            count += 1

        if count != len(self.graph):
            print ('cycle exists')
            return []
        else:
            print ('cycle does NOT exists')
            return order

        
    def prims_min_spanning_tree(self):
        mst_set = set()
        key_values = {i:math.inf for i in self.graph.keys()}
        vertex = list(self.graph.keys())[0]
        key_values[vertex] = 0

        def return_min_value_vertex(mst_set, key_values):
            min_value = math.inf
            for vertex in self.graph:
                if vertex not in mst_set:
                    if key_values[vertex] < min_value:
                        min_value = key_values[vertex]
                        min_vertex = vertex
            return min_vertex

        while len(mst_set) != len(self.graph.keys()):
            vertex = return_min_value_vertex(mst_set, key_values)
            mst_set.add(vertex)
            for neighbour in self.graph[vertex]:
                if neighbour[0] not in mst_set:
                    key_values[neighbour[0]] = min(key_values[neighbour[0]], neighbour[1])
            
        return key_values

    def prims_min_spanning_tree_efficient(self):
        mst_set = set()
        heap = [(0, 0)] # (initial_distance, start_vertex)
        heapify(heap)
        key_values = {i:math.inf for i in self.graph.keys()}
        key_values[0] = 0

        while len(mst_set) != len(self.graph.keys()):
            min_dist, min_vertex = heappop(heap)
            mst_set.add(min_vertex)

            for vertex, distance in self.graph[min_vertex]:
                if vertex not in mst_set:
                    if distance < key_values[vertex]:
                        key_values[vertex] = distance
                        heappush(heap, (distance, vertex))
        
        return key_values

                    
    def dijkstra_path(self, start):
        dist_values = {i:math.inf for i in self.graph}
        dist_values[start] = 0
        # to store path as well
        path_values = {i:[] for i in self.graph}
        path_values[start] = []

        spt_set = []

        def return_min_value_vertex(spt_set, dist_values):
            min_vertex_value = math.inf
            for vertex in self.graph:
                if vertex not in spt_set:
                    if dist_values[vertex] < min_vertex_value:
                        min_vertex_value = dist_values[vertex]
                        min_vertex = vertex
            return min_vertex

        while len(spt_set) < len(self.graph):
            vertex = return_min_value_vertex(spt_set, dist_values)
            spt_set.append(vertex)

            for neighbour in self.graph[vertex]:
                if neighbour[0] not in spt_set:
                    # dist_values[neighbour[0]] = min(dist_values[neighbour[0]], neighbour[1]+dist_values[vertex])
                    if neighbour[1] + dist_values[vertex] < dist_values[neighbour[0]]:
                        dist_values[neighbour[0]] = neighbour[1] + dist_values[vertex]
                        path_values[neighbour[0]] = path_values[vertex] + [vertex]
                        
        print (path_values)
        return dist_values

    def dijkstra_path_efficient(self, start):
        
        heap = [(0, start)]
        heapify(heap)
        dist_values = {i:math.inf for i in self.graph}
        dist_values[start] = 0
        mst_set = set()

        while len(mst_set) != len(self.graph.keys()):
            min_distance, min_vertex = heappop(heap)
            mst_set.add(min_vertex)

            for neighbour, distance in self.graph[min_vertex]:
                if neighbour not in mst_set:
                    if dist_values[min_vertex] + distance < dist_values[neighbour]:
                        dist_values[neighbour] = dist_values[min_vertex] + distance
                        heappush(heap, (dist_values[neighbour], neighbour))
        
        return dist_values

    def bellman_ford(self, start, n):
        dist_values = {i:math.inf for i in self.graph.keys()}
        dist_values['C'] = math.inf
        dist_values[start] = 0
        path_values = {i:[] for i in self.graph.keys()}
        path_values[start] = [start]
        path_values['C'] = []

        for i in range(n-1):
            for src in self.graph:
                for tgt, distance in self.graph[src]:
                    # check for infinity so we know that src vertex is discovered
                    if dist_values[src] != math.inf and dist_values[src] + distance < dist_values[tgt]:
                        dist_values[tgt] = dist_values[src] + distance
                        path_values[tgt] = path_values[src] + [tgt]

        for src in self.graph:
            for tgt, distance in self.graph[src]:
                if dist_values[src] != math.inf and dist_values[src] + distance < dist_values[tgt]:
                    print ('Graph has negative weight cycle')
                    return

        print (path_values)
        return dist_values

    def floyd_warshall(self, graph, n):
        output = graph
        # path_values = [[None]*n]*n
        # for i in range(n):
        #     for j in range(n):
        #         if i == j:
        #             path_values[i][j] = i

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if output[i][j] > output[i][k] + output[k][j]:
                        output[i][j] = output[i][k] + output[k][j]
                        # path_values[i][j] = path_values[i][k] + path_values[k][j]


        # print (path_values)
        return output

                
# g = Graph()
# g.add_edge(0, 1)  # comment this line to make graph disconnected
# g.add_edge(0, 2) 
# g.add_edge(1, 2) 
# g.add_edge(2, 0) 
# g.add_edge(2, 3)
# g.add_edge(3, 3)

# print ('Graph representation using adjacency list is {}'.format(g.graph))
# print ('******')

# print ('bfs of a graph')
# output = []
# g.bfs_disconnected(2, output)
# print ('bfs of the graph is {}'.format(output))

# print ('dfs of a graph')
# output = []
# g.dfs_disconnected(0, output)
# print ('dfs of the graph is {}'.format(output))

# all the mother veretxes
# g.find_mother_vertex()

# mother vertex efficient method
# g.mother_vertex_efficient()

# vertex at given level
# output = []
# level = 2
# g.nodes_at_given_level_bfs(start = 2, level = level, output = output)
# print ('nodes at {} level are {}'.format(level, output))

# find path between 2 vertices
# path = []
# src = 0
# dest = 2
# path = g.find_path_between_2_vertices(src, dest, path)
# print ('path between {} and {} is {}'.format(src, dest, path))

# all paths between src and dest
# output = []
# path = []
# src = 0
# dest = 2
# g.all_possible_paths(src, dest, path, output)
# print ('all paths between {} and {} are {}'.format(src, dest, output))

# min path between 2 vertex
# output = []
# path = []
# src = 0
# dest = 2
# g.min_path_between_2_vertex(src, dest, path, output)
# print ('min path between {} and {} are {}'.format(src, dest, output))

# min path between 2 vertices using bfs
# print ('min path is - {}'.format(g.min_path_between_2_vertex_bfs(0, 2)))

# detect cycle in directed graph using dfs
# has_cycle = g.detect_cycle_directed()
# print (str(has_cycle))

# detect cycle in undirected graph using dfs
# g1 = Graph()
# g1.add_edge_undirected(0, 1)  # comment this line to make graph disconnected
# g1.add_edge_undirected(0, 2) 
# g1.add_edge_undirected(1, 2) 
# g1.add_edge_undirected(0, 3)
# g1.add_edge_undirected(3, 3)
# g1.add_edge_undirected(3, 4)
# has_cycle = g1.detect_cycle_undirected_dfs()
# print (str(has_cycle))

# detect cycle using union find
# g1 = Graph()
# g1.add_edge_undirected(0, 1)  # comment this line to make graph disconnected
# g1.add_edge_undirected(0, 2) 
# g1.add_edge_undirected(2, 3)
# print ('cycle is there - {}'.format(g1.detect_cycle_undirected_union_find()))

# topological sort
g1 = Graph()
g1.add_edge(5, 2) 
g1.add_edge(5, 0) 
g1.add_edge(4, 0) 
g1.add_edge(4, 1) 
g1.add_edge(2, 3) 
g1.add_edge(3, 1)

print ('topological sort is - {}'.format(g1.topological_sort()))

print ('topological sort is - {}'.format(g1.topological_sort_kahns_indegree()))

# prims mst
# g1 = Graph()
# g1.add_edge_with_weight_undirected(0,1,4)
# g1.add_edge_with_weight_undirected(1,2,8)
# g1.add_edge_with_weight_undirected(2,3,7)
# g1.add_edge_with_weight_undirected(3,4,9)
# g1.add_edge_with_weight_undirected(5,4,10)
# g1.add_edge_with_weight_undirected(6,5,2)
# g1.add_edge_with_weight_undirected(7,6,1)
# g1.add_edge_with_weight_undirected(0,7,8)
# g1.add_edge_with_weight_undirected(1,7,11)
# g1.add_edge_with_weight_undirected(7,8,7)
# g1.add_edge_with_weight_undirected(2,8,2)
# g1.add_edge_with_weight_undirected(8,6,6)
# g1.add_edge_with_weight_undirected(2,5,4)
# g1.add_edge_with_weight_undirected(3,5,14)
# print ('key values is - {}'.format(g1.prims_min_spanning_tree()))


# prims mst efficient
# g1 = Graph()
# g1.add_edge_with_weight_undirected(0,1,4)
# g1.add_edge_with_weight_undirected(1,2,8)
# g1.add_edge_with_weight_undirected(2,3,7)
# g1.add_edge_with_weight_undirected(3,4,9)
# g1.add_edge_with_weight_undirected(5,4,10)
# g1.add_edge_with_weight_undirected(6,5,2)
# g1.add_edge_with_weight_undirected(7,6,1)
# g1.add_edge_with_weight_undirected(0,7,8)
# g1.add_edge_with_weight_undirected(1,7,11)
# g1.add_edge_with_weight_undirected(7,8,7)
# g1.add_edge_with_weight_undirected(2,8,2)
# g1.add_edge_with_weight_undirected(8,6,6)
# g1.add_edge_with_weight_undirected(2,5,4)
# g1.add_edge_with_weight_undirected(3,5,14)
# print ('key values is - {}'.format(g1.prims_min_spanning_tree_efficient()))

# dijkstra
# g1 = Graph()
# g1.add_edge_with_weight_undirected(0,1,4)
# g1.add_edge_with_weight_undirected(1,2,8)
# g1.add_edge_with_weight_undirected(2,3,7)
# g1.add_edge_with_weight_undirected(3,4,9)
# g1.add_edge_with_weight_undirected(5,4,10)
# g1.add_edge_with_weight_undirected(6,5,2)
# g1.add_edge_with_weight_undirected(7,6,1)
# g1.add_edge_with_weight_undirected(0,7,8)
# g1.add_edge_with_weight_undirected(1,7,11)
# g1.add_edge_with_weight_undirected(7,8,7)
# g1.add_edge_with_weight_undirected(2,8,2)
# g1.add_edge_with_weight_undirected(8,6,6)
# g1.add_edge_with_weight_undirected(2,5,4)
# g1.add_edge_with_weight_undirected(3,5,14)
# print ('key values is - {}'.format(g1.dijkstra_path(0)))

# dijkstra efficient
# g1 = Graph()
# g1.add_edge_with_weight_undirected(0,1,4)
# g1.add_edge_with_weight_undirected(1,2,8)
# g1.add_edge_with_weight_undirected(2,3,7)
# g1.add_edge_with_weight_undirected(3,4,9)
# g1.add_edge_with_weight_undirected(5,4,10)
# g1.add_edge_with_weight_undirected(6,5,2)
# g1.add_edge_with_weight_undirected(7,6,1)
# g1.add_edge_with_weight_undirected(0,7,8)
# g1.add_edge_with_weight_undirected(1,7,11)
# g1.add_edge_with_weight_undirected(7,8,7)
# g1.add_edge_with_weight_undirected(2,8,2)
# g1.add_edge_with_weight_undirected(8,6,6)
# g1.add_edge_with_weight_undirected(2,5,4)
# g1.add_edge_with_weight_undirected(3,5,14)
# print ('key values is - {}'.format(g1.dijkstra_path_efficient(0)))

# bellman ford
# g1 = Graph()
# g1.add_edge_with_weight('A','B',-1)
# g1.add_edge_with_weight('A','C',4)
# g1.add_edge_with_weight('B','C',3)
# g1.add_edge_with_weight('B','D',2)
# g1.add_edge_with_weight('B','E',2)
# g1.add_edge_with_weight('D','C',5)
# g1.add_edge_with_weight('D','B',1)
# g1.add_edge_with_weight('E','D',-3)
# print ('dist values is - {}'.format(g1.bellman_ford('A', 6)))

# floyd warshall
# g1 = Graph()
# graph = [
#     [0,5,math.inf,10], 
#     [math.inf,0,3,math.inf], 
#     [math.inf, math.inf, 0,   1], 
#     [math.inf, math.inf, math.inf, 0] 
# ]

# print ('dist values is - {}'.format(g1.floyd_warshall(graph, 4)))
