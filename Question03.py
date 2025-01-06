import sys
import math
from itertools import combinations

INF = math.inf

sys.stdin = open("answer.txt")

n = int(input())
E = [list(map(int, input().split())) for _ in range(n)]
E_TF = [False] * n

min_val = INF
## 공평하게 절반씩 나누어 진행

def cal_eff():
    a_eff = 0
    b_eff = 0

    A_team = [i for i, val in enumerate(E_TF) if val]
    B_team = [i for i, val in enumerate(E_TF) if not val]

    for a in combinations(A_team, 2):
        a_eff += E[a[0]][a[1]] + E[a[1]][a[0]]
    for b in combinations(B_team, 2):
        b_eff += E[b[0]][b[1]] + E[b[1]][b[0]]

    return abs(a_eff-b_eff)


def sol(idx):
    global min_val

    if E_TF.count(True) == n//2:
        min_val = min(min_val, cal_eff())
        return

    # n명 중 절반 뽑기
    for i in range(idx, n):
        if not E_TF[i]:
            E_TF[i] = True
            sol(i+1)
            E_TF[i] = False

sol(0)
print(min_val)