from DP_LCS import DP_LCS 
from DP_multistage_G import DP_multistage_G
import random

def example_DP_multistage_G():
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
                        end='11',
                        print_out=True)
    # solve multistage graph problem with Dynamic Programming method
    test_dp.dp_shortest_path()
    # show result
    test_dp.print_path()

def example_DP_LCS():
    sa = 'w1a22n3g4l5e6i'
    sb = '123456'
    dp_lcs = DP_LCS(sa, sb)
    dp_lcs.dp_search()
    dp_lcs.dp2LCSequence()
    dp_lcs.show_dp_matrix()
    print('LCS', dp_lcs.lcs)

if __name__ == '__main__':
    example_DP_multistage_G()
    example_DP_LCS()