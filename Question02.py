import sys
import math
from collections import deque

INF = math.inf

sys.stdin = open("answer.txt")

n, m = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(n)]
min_val = INF

houses = deque()
stores = deque()

for i in range(n):
    for j in range(n):
        if A[i][j] == 1:
            houses.append((i, j))
        elif A[i][j] == 2:
            stores.append((i, j))
stores_TF = [False] * len(stores)
# 3 1
# 1 0 0
# 0 2 2
# 0 1 0

# 1 HOWSE, 2 STORE

def cal_dist():
    res = 0
    for i, j in houses:             # 각 아파트 마다 편의점의 거리를 계산하여 가장 짧은거리 합
        min_dist = INF
        for k in range(len(stores)):
            if stores_TF[k]:
                min_dist = min(min_dist, abs(stores[k][0]-i)+abs(stores[k][1]-j))
        res += min_dist

    return res

def sol(cnt):
    global min_val

    if cnt == m:
        min_val = min(min_val, cal_dist())

    for i in range(len(stores)):
        if stores_TF[i] == False:
            stores_TF[i] = True
            sol(cnt+1)
            stores_TF[i] = False

sol(0)
print(min_val)