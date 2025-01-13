import sys
sys.stdin = open("answer.txt")
sys.setrecursionlimit(10**7)

import math
from copy import deepcopy
INF = math.inf
#asdasdas
moves = [
    [],
    [-1, 0], [-1, -1], [0, -1], [1, -1],   # ↑, ↖, ←, ↙
    [1, 0], [1, 1], [0, 1], [-1, 1]        # ↓, ↘, →, ↗
]

group = []

for _ in range(4):
    temp = []
    A = list(map(int, input().split()))
    for i in range(0, 8, 2):
        temp.append([A[i], A[i+1]])
    group.append(temp)
max_val = -INF
# # 개구리 0, 0 사냥
# group[0][0] = [-1, group[0][0][1]]


# 12 7 13 3 4 4 3 1 (12번 개구리 7번 방향) (13번 개구리 3번 방향 )...
# 5 1 1 8 8 7 15 4   ....
# 9 5 2 5 14 3 7 5   ....
# 11 7 10 8 16 3 6 3 ....

# [-1, 7] [13, 3] [4, 4] [3, 1]
# [5, 1] [1, 8] [8, 7] [15, 4]
# [9, 5] [2, 5] [14, 3] [7, 5]
# [11, 7] [10, 8] [16, 3] [6, 3]

# 개구리는 0,0 위치의 파리를 사냥하며 시작. 잡아먹은 파리 그룹의 이동방향으로 고정
# 파리 그룹 자신의 방향을 이동. 이동할 수 없을 경우 45도 반시계 방향으로 회전 -> move += 1, 무조건 이동하며 개구리가 있는칸은 못감.
# 해당위치에 있던 파리와 자리 바꿈
# 개구리 -> 해당 방향의 어느 칸으로도 점프 할 수 있다.
# 개구리가 이동할 수 없는 곳이라면, 사냥을 멈춘다.

# 모든 곳을 생각해봐야함
# 파리는 [그룹, 방향] 으로 관리
# 개구리 == -1
def move_group(state):
    for group_idx in range(1, 17):
        flag = False
        for i in range(4):
            for j in range(4):
                # 파리의 번호가 해당 번호라면?
                if state[i][j] != [] and state[i][j][0] == group_idx:
                    flag = True
                    di = i + moves[state[i][j][1]][0]
                    dj = j + moves[state[i][j][1]][1]
                    # 이동할 수 없을 경우
                    if not 0<=di<4 or not 0<=dj<4 or state[di][dj][0] == -1:
                        while True:
                            if state[i][j][1] == 8: state[i][j][1] = 1
                            else: state[i][j][1] += 1

                            di = i + moves[state[i][j][1]][0]
                            dj = j + moves[state[i][j][1]][1]
                            if not 0 <= di < 4 or not 0 <= dj < 4 or state[di][dj][0] == -1:
                                continue
                            else:
                                state[di][dj], state[i][j] = state[i][j], state[di][dj]
                                break
                    # 이동할 수 있는 경우
                    else: state[di][dj], state[i][j] = state[i][j], state[di][dj]

                if flag: break
            if flag: break

def sol(r, c, state, cnt, pr, pc):
    global max_val

    # 개구리가 해당 위치 사냥.
    cnt += state[r][c][0]
    max_val = max(max_val, cnt)

    state[r][c] = [-1, state[r][c][1]]
    if pr == -1: pass
    else:
        state[pr][pc] = [0, 0]

    # 만약 개구리가 이동할 방향이 없다면 최댓값 업데이트 후 return
    if not 0<=r + moves[state[r][c][1]][0]<4 or not 0<=c+moves[state[r][c][1]][1]<4:
        return

    # 파리그룹 이동
    move_group(state)

    # 개구리 위치 선택 (해당 방향의 어느 칸으로도 점프 할 수 있다.)
    rr, cc = r, c
    while True:
        dr = rr + moves[state[r][c][1]][0]
        dc = cc + moves[state[r][c][1]][1]

        if not 0<=dr<4 or not 0<=dc<4:
            break

        if state[dr][dc] == [0, 0]:
            rr, cc = dr, dc
            continue
        state_b = deepcopy(state)
        sol(dr, dc, state_b, cnt, r, c)
        rr, cc = dr, dc

sol(0, 0, group, 0, -1, -1)
print(max_val)

