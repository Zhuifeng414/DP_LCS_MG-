from naive_G import naive_G

class DP_multistage_G(naive_G):
    def __init__(self,
                nodes, 
                edges, 
                direct=True, 
                weight=True, 
                adj_type='list', 
                start=None, 
                end=None,
                print_out=True):
        super().__init__(nodes, 
                        edges, 
                        direct=direct, 
                        weight=weight, 
                        adj_type=adj_type)
        self.start = start 
        self.end = end
        self.level_nodes = self.get_level_nodes()
        self.path = []
        self.min_cost = -1
        self.print_out = print_out
        
    def get_level_nodes(self):
        self.bfs(self.start)
        level_nodes = {}
        max_s = -1
        min_s = 1e3
        for node in self.G.nodes:
            if self.G.nodes[node]['d'] not in level_nodes:
                level_nodes[self.G.nodes[node]['d']] = []
            if node not in level_nodes[self.G.nodes[node]['d']]:
                level_nodes[self.G.nodes[node]['d']].append(node)
                if self.G.nodes[node]['d'] > max_s:
                    max_s = self.G.nodes[node]['d']
                if self.G.nodes[node]['d'] < min_s:
                    min_s = self.G.nodes[node]['d']
        return level_nodes

    def dp_shortest_path(self):
        s = self.G.nodes[self.end]['d']
        self.cost = {s:{self.end: {'cost':0, 'next_s':None, 'next_node':None}}}
        Q = [self.end]
        while len(Q) > 0 and s>0:
            self.end = Q.pop(0)
            s -= 1
            self.cost[s] = {}
            for pre_n in self.level_nodes[s]:
                min_cost = 1e3
                min_next_n = None
                for next_n in self.G.get_adj(pre_n):
                    edge_weight = self.G.get_edge_weight(pre_n, next_n)
                    if edge_weight + self.cost[s+1][next_n]['cost'] < min_cost:
                        min_cost = edge_weight + self.cost[s+1][next_n]['cost']
                        min_next_n = next_n
                self.cost[s][pre_n] ={'cost':min_cost, 'next_s':s+1, 'next_node':min_next_n}
                Q.append(pre_n)
        return 
    
    def print_path(self):
        if self.print_out:
            print('Get Cost results as follow:')
            for k, v in self.cost.items():
                print('stage =',k, v)
            print('=============================>')

        s = self.G.nodes[self.start]['d']
        min_cost = 1e3
        
        for node in self.cost[s]:
            if self.cost[s][node]['cost'] < min_cost:
                min_cost = self.cost[s][node]['cost']
                min_node = node 
        self.min_cost = min_cost
        
        while s is not None:
            if self.print_out:
                print('s:{}, path_node:{}, min_cost:{}'.format(s, min_node, self.cost[s][min_node]['cost']))
            self.path.append(min_node)
            next_s = self.cost[s][min_node]['next_s']
            next_node = self.cost[s][min_node]['next_node']
            s = next_s
            min_node = next_node
        if self.print_out:
            print('Minimum cost path is: {} with totally cost {}'.format(self.path, self.min_cost))
        return 

if __name__ == '__main__':
    nodes = ['1', '2', '3', '4', '5', '6',
    '7', '8', '9', '10', '11']

    edges = [
        ['1', '2', 7], ['1', '3', 8], ['1', '4', 6],
        ['2', '5', 9], ['2', '8', 8],
        ['3', '6', 7], ['3', '7', 6], 
        ['4', '5', 4], ['4', '7', 3], ['4', '8', 3],
        ['5', '9', 7], ['5', '10', 6],
        ['6', '9', 5], 
        ['7', '9', 4], ['7', '10', 7],
        ['8', '9', 5],
        ['9', '11', 4],
        ['10', '11', 3]
    ]
    
    # generate DP_multistage_G class dp, input G, start node and end node
    test_dp = DP_multistage_G(
                        nodes, 
                        edges, 
                        direct=True, 
                        weight=True, 
                        adj_type='list', 
                        start='1', 
                        end='11')
    # solve multistage graph problem with Dynamic Programming method
    test_dp.dp_shortest_path()
    # show result
    test_dp.print_path()