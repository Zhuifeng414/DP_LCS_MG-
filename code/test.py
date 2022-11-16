from DP_LCS import DP_LCS 
from DP_multistage_G import DP_multistage_G
import time
import random

def Intergration_test_DP_multistage_G(test_num, adj_type='list'):
    error_count = 0
    for i in range(test_num):
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

        fake_index = random.randint(0,len(edges)-1)
        fake_edge = edges[fake_index][:2]
        edges[fake_index][2] = -100
        # generate DP_multistage_G class dp, input G, start node and end node
        test_dp = DP_multistage_G(
                            nodes, 
                            edges, 
                            direct=True, 
                            weight=True, 
                            adj_type=adj_type, 
                            start='1', 
                            end='11',
                            print_out=False)
        # solve multistage graph problem with Dynamic Programming method
        test_dp.dp_shortest_path()
        # show result
        test_dp.print_path()
        
        if fake_edge[0] in test_dp.path and fake_edge[1] in test_dp.path:
            #print('correct with fake_index =', fake_index)
            pass 
        else:
            error_count += 1
            print('##error! fake_index =', fake_index, fake_edge)
            print(test_dp.path)
            print(fake_edge)
            print(test_dp.cost)
    print('error rate is :{}%'.format(round(1.0*error_count/test_num*100,2)))

def random_len_str(str_len=5, list_index=0):
    char_list0 = 'abcdefghijklmnopqr'
    char_list1 = 'stuvwxyz1234567890'
    if list_index == 0:
        char_list = char_list0
    else:
        char_list = char_list1
    rand_str = ''
    for i in range(str_len):
        rand_index = random.randint(0,len(char_list)-1)
        rand_str += char_list[rand_index]
    return rand_str

def randm_list(max_len, list_len):
    rand_res = []
    times = 0
    while len(rand_res) < list_len:
        rand_int = random.randint(0, max_len)
        if rand_int not in rand_res:
            rand_res.append(rand_int)
        times +=1
        if times > 1000:
            print('randm_list failed!')
            break
    return sorted(rand_res)     

def str_replace(input_str, rand_index_list):
    replace_str = '+-*/#><()[]$'
    if len(rand_index_list) > len(replace_str):
        print('str_replace error!')
    else:
        for i in range(len(rand_index_list)):
            input_str = input_str[:rand_index_list[i]]+replace_str[i]+input_str[rand_index_list[i]:]
    return input_str

def generate_lcs_pair(sa_len=6, sb_len=8, lcs_len=5):
    replace_str = '+-*/#><()[]$'
    sa = random_len_str(sa_len, list_index=0)
    sb = random_len_str(sb_len, list_index=1)
    rand_index_sa = randm_list(sa_len-1, lcs_len)
    rand_index_sb = randm_list(sb_len-1, lcs_len)
    sa = str_replace(sa, rand_index_sa)
    sb = str_replace(sb, rand_index_sb)
    lcs_str = replace_str[:lcs_len]
    return sa, sb, lcs_str

def Intergration_test_DP_LCS(test_num=100):
    error_count = 0
    for i in range(test_num):
        sa_len = random.randint(8,20)
        sb_len = random.randint(8,30)
        lcs_len = random.randint(1,7)
        sa, sb, lcs_str = generate_lcs_pair(sa_len, sb_len, lcs_len)
        dp_lcs = DP_LCS(sa, sb)
        dp_lcs.dp_search()
        dp_lcs.dp2LCSequence()
        if len(dp_lcs.lcs) == len(lcs_str) and dp_lcs.lcs == lcs_str:
            #print('Yes, I Do !')
            pass 
        else:
            error_count +=1
            print('error!', sa, sb, lcs_str, dp_lcs.lcs)
    print('error rate is :{}%'.format(round(1.0*error_count/test_num*100,2)))
    
if __name__ == '__main__':
    print('Intergration_test_DP_multistage_G(List) 1000 test case' )
    t1 = time.time()
    Intergration_test_DP_multistage_G(1000, adj_type='list')
    t2 = time.time()
    print("Time cost for Intergration_test_DP_multistage_G(List) is:", t2-t1)

    print('Intergration_test_DP_multistage_G(Matrix) 1000 test case' )
    t3 = time.time()
    Intergration_test_DP_multistage_G(1000, adj_type='array')
    t4 = time.time()
    print("Time cost for Intergration_test_DP_multistage_G(Matrix) is:", t4-t3)

    print('Intergration_test_DP_LCS 1000 test case')
    Intergration_test_DP_LCS(1000)
    t3 = time.time()
    print("Time cost for Intergration_test_DP_LCS is:", t3-t2)