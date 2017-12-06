class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def sub_find(queen,temp_dif,temp_sum):
            p=len(queen)
            if p==n:
                result.append(queen)
                return
            for i in range(n):
                if i not in queen and i+p not in temp_sum and i-p not in temp_dif:
                    sub_find(queen+[i],temp_dif+[i-p],temp_sum+[i+p])
        result=[]
        sub_find([],[],[])
        return [['.'*i+'Q'+'.'*(n-i-1) for i in each] for each in result ]
        