import numpy as np
def extend_array_once(arr):
    b = np.zeros([1, arr.shape[0]])
    arr = np.row_stack((arr ,b))
    b = np.zeros([1, arr.shape[0]])
    arr = np.column_stack((arr, b.T))
    return arr

class naive_G_adj_array(object):
    def __init__(self, nodes, edges, direct=True, weight=False, adj_type='array'):
        self.time = 0
        self.adj_type = adj_type
        self.node_num = 0
        self.nodes_map = {}
        self.nodes = {}
        self.edges = np.zeros([1, 1])
        self.add_nodes(nodes)
        self.add_edges(edges, direct=direct, weight=weight)
        return 

    def get_adj(self, node):
        node_index = self.nodes[node]['node_index']
        adj_index = self.edges[node_index, :].nonzero()[0].tolist()
        return [self.nodes_map[item] for item in adj_index]
    
    def add_nodes(self, nodes):
        nodes = list(set(nodes))
        nodes.sort()
        for node in nodes:
            if node not in self.nodes:
                self.node_num += 1
                self.nodes_map[self.node_num] = node
                self.nodes[node] = {
                    'node_index': self.node_num, 
                    'd': -1, 
                    'f': -1, 
                    'color': -1,
                    'pre': None}   
                self.edges = extend_array_once(self.edges)
        return 

    def add_edges(self, edges, direct=True, weight=False):
        if self.adj_type == 'array':
            if weight is False:
                for p, q in edges:
                    self.edges[self.nodes[p]['node_index'], self.nodes[q]['node_index']] = 1
                    if direct is False:
                        self.edges[self.nodes[q]['node_index'], self.nodes[p]['node_index']] = 1
                
            if weight is True:
                for p, q, w in edges:
                    self.edges[self.nodes[p]['node_index'], self.nodes[q]['node_index']] = w
                    if direct is False:
                        self.edges[self.nodes[q]['node_index'], self.nodes[p]['node_index']] = w             
        return
    
    def get_edge_weight(self, u, v):
        u_index = self.nodes[u]['node_index']
        v_index = self.nodes[v]['node_index']
        return self.edges[u_index, v_index]
  
class naive_G_adj_list(object):
    def __init__(self, nodes, edges, direct=True, weight=False, adj_type='list'):
        self.time = 0
        self.adj_type = adj_type
        self.nodes = {}
        self.edges = {}
        self.inverse_edges = {}
        self.add_nodes(nodes)
        self.add_edges(edges, direct=direct, weight=weight) 
        return 

    def get_adj(self, node):
        return sorted(list(self.edges[node].keys()))
           
    def add_nodes(self, nodes):
        nodes = list(set(nodes))
        nodes.sort()
        for node in nodes:
            if node not in self.nodes:
                self.nodes[node] = {
                    'node_index': node, 
                    'd': -1, 
                    'f': -1, 
                    'color': -1,
                    'pre': None} 
            self.edges[node] = {}
        return 

    def add_edges(self, edges, direct=True, weight=True):
        if weight is False:
            for p, q in edges:
                self.edges[p][q] = {'weight':1}
                if direct is False:
                    self.edges[q][p] = {'weight':1}

        if weight is True:
            for p, q, w in edges:
                self.edges[p][q] = {'weight':w}
                if direct is False:
                    self.edges[q][p] = {'weight':w}
        return

    def get_edge_weight(self, u, v):
        return self.edges[u][v]['weight']

class naive_G(object):
    def __init__(self, nodes, edges, direct=True, weight=False, adj_type='list'):
        if adj_type == 'list':
            self.G = naive_G_adj_list(nodes, edges, direct=direct, weight=weight, adj_type='list')
        elif adj_type == 'array':
            self.G =  naive_G_adj_array(nodes, edges, direct=direct, weight=weight, adj_type='array')
        else:
            print('adj_type error!')
            return

    def dfs(self):
        for node in self.G.nodes:
            # White: un-discovered
            self.G.nodes[node]['color'] = 'white' 
            self.G.nodes[node]['pre'] = None 
        # record number of steps
        self.G.time = 0
        for node in self.G.nodes:
            if self.G.nodes[node]['color'] == 'white':
                self.dfs_visit(node)
        return 

    def dfs_visit(self, node):
        self.G.time = self.G.time+1
        self.G.nodes[node]['d'] = self.G.time 
        # Gray: discovered, visited, not done
        self.G.nodes[node]['color'] = 'gray'
        # explore each edge (u,v)
        for v_node_index in self.G.get_adj(node): 
            if self.G.nodes[v_node_index]['color'] == 'white':
                self.G.nodes[v_node_index]['pre'] = node
                self.dfs_visit(v_node_index)
        self.G.time = self.G.time + 1
        self.G.nodes[node]['f'] = self.G.time 
        # Black: Done
        self.G.nodes[node]['color'] = 'black'
        return

    def bfs(self, s):
        for node in self.G.nodes:
            if node != s:
                self.G.nodes[node]['color'] = 'white'
                self.G.nodes[node]['d'] = np.inf
                self.G.nodes[node]['pre'] = None 
        self.G.nodes[s]['color'] = 'gray'
        self.G.nodes[s]['d'] = 0
        self.G.nodes[s]['pre'] = None 
        Q = []
        Q.append(s)
        while len(Q) > 0:
            u = Q.pop(0)
            for v in self.G.get_adj(u):
                if self.G.nodes[v]['color'] == 'white':
                    self.G.nodes[v]['color'] = 'gray'
                    self.G.nodes[v]['d'] = self.G.nodes[u]['d'] + 1
                    self.G.nodes[v]['pre'] = u
                    Q.append(v)
        self.G.nodes[u]['color'] = 'black'
        return 

