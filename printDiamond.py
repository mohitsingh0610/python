class Solution:
    def printDiamond(self, N):
        #code here
        for i in range(0, N):
            for j in range(0, N-i-1):
                print(' ', end='')
            for j in range(0, i+1):
                print('* ', end = '')
            print()
        for i in range(N, 0, -1):
            for j in range(0, N-i):
                print(' ', end='')
            for j in range(0, i):
                print('* ', end = '')
            print()
                
            


                   
Solution().printDiamond(7)           