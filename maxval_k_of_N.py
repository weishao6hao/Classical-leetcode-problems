#coding=utf-8
import numpy as np
'''
题目描述：
    有 n 个学生站成一排，每个学生有一个能力值，牛牛想从这 n 个学生中按照顺序选取 k 名学生，
    要求相邻两个学生的位置编号的差不超过 d，使得这 k 个学生的能力值的乘积最大，你能返回最大的乘积吗？
    每个输入包含 1 个测试用例。每个测试数据的第一行包含一个整数 n (1 <= n <= 50)，表示学生的个数，
    接下来的一行，包含 n 个整数，按顺序表示每个学生的能力值 ai（-50 <= ai <= 50）。
    接下来的一行包含两个整数，k 和 d (1 <= k <= 10, 1 <= d <= 50)。
'''
a = np.zeros(55)
n = int(input('n:'))
for i in range(n):
    a[i] = int(input('a[%d]'% i))
k = int(input('k:'))
d = int(input('d:'))
res = float('-inf')
maxval = np.zeros((55,15))
minval = np.zeros((55,15))

for i in range(n):
    maxval[i,0] = a[i]
    minval[i,0] = a[i]
for i in range(n):
    for j in range(1,k):
        for t in range(i-1,max(0,i-d)-1,-1):
            maxval[i][j] = max(maxval[i,j],max(maxval[t,j-1]*a[i],minval[t,j-1]*a[i]))
            minval[i][j] = min(minval[i,j],min(minval[t,j-1]*a[i],maxval[t,j-1]*a[i]))
    res = max(res,maxval[i,j])
print('res: %d'%res)