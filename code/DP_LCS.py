class DP_LCS(object):
    def __init__(self, sa, sb, print_out=False):
        self.sa = sa 
        self.sb = sb 
        self.lcs = ''
        self.print_out = print_out
        self.dp = [[0 for i in range(len(sb)+1)] for j in range(len(sa)+1)]
        return

    def dp_search(self):
        if len(self.sa) == 0 or len(self.sb) == 0:
            return 0
        
        for i in range(0, len(self.sa)+1):
            for j in range(1, len(self.sb)+1):
                if i==0 and j==0:
                    self.dp[i][j] = 0
                elif self.sa[i-1] == self.sb[j-1]:
                    self.dp[i][j] = self.dp[i-1][j-1] + 1
                else:
                    self.dp[i][j] = max(self.dp[i-1][j], self.dp[i][j-1])
       

    def dp2LCSequence(self):
        i = len(self.sa)
        j = len(self.sb)
        index = self.dp[i-1][j-1]
        while index >= 0:
            if self.print_out:
                print('i={}, j={}, sa[i]={}, sb[j]={}, \n\
                    dp[i-1][j-1]={}, dp[i-1][j]={}, \n\
                    dp[i][j-1]={}, dp[i][j]={}'.format(\
                        i, j, self.sa[i-1], self.sb[j-1],\
                            self.dp[i-1][j-1], self.dp[i-1][j],\
                            self.dp[i][j-1], self.dp[i][j]))

            if i > 0 and self.dp[i][j] == self.dp[i-1][j]:
                if self.print_out:
                    print('i--')
                i -= 1
            elif j > 0 and self.dp[i][j] == self.dp[i][j-1]:
                if self.print_out:
                    print('j--')
                j -= 1
            else:
                if i-1>=0:
                    self.lcs += self.sa[i-1]
                index -=1
                i -= 1
                j -= 1
            if self.print_out:
                print('###lcs', self.lcs)
        self.lcs = self.lcs[::-1]
    
    def show_dp_matrix(self):
        print('=============>>>>')
        print('sb: '+'  '.join(list(self.sb)))
        xsa = ['sa']+list(self.sa)
        for i in range(len(self.dp)):
            item = self.dp[i]
            print(item, xsa[i])
        print('=============>>>>')



if __name__ == '__main__':
    sa = 'w1a22n3g4l5e6i'
    sb = '123456'
    dp_lcs = DP_LCS(sa, sb)
    dp_lcs.dp_search()
    dp_lcs.dp2LCSequence()
    dp_lcs.show_dp_matrix()
    print('LCS', dp_lcs.lcs)