import sys
sys.stdin = open("answer.txt")

N, M = map(int, input().split())  # 교실의 세로, 가로 크기
MAP = []  # 교실의 벽 정보
MACHINE_LIST = []  # 방역기 정보 리스트 (위치, 타입)

ans = 1e10  # 방역 되지 않은 칸의 최솟값

machine_rotated_list = []  # 방역기들의 회전 횟수 (0 ~ 3)

# 타입별 소독약을 뿌리는 방향 (0 ~ 3, 북동남서)
disinfect_dir = [
    [],
    [0, 1, 0, 0],  # 1번 방역기
    [0, 1, 0, 1],  # 2번 방역기
    [1, 1, 0, 0],  # 3번 방역기
    [1, 1, 0, 1],  # 4번 방역기
    [1, 1, 1, 1]  # 5번 방역기
]

# 타입별 방역기를 회전 시킬 횟수 (1 ~ 5, 첫번째는 빈칸)
machine_can_rotate = [0, 4, 2, 4, 4, 1]

# 북동남서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for r in range(N):
    data = list(map(int, input().split()))
    for c in range(M):
        if 1 <= data[c] <= 5: MACHINE_LIST.append([r, c, data[c]])
    MAP.append(data)


def get_area():
    disinfected = [[False] * M for _ in range(N)]  # 방역한 칸 정보
    # 방역기 별로 교실 방역 수행하기
    for [row, col, rot, t] in machine_rotated_list:
        # 4 방향에 대해서 방역 수행
        disinfected[row][col] = True
        for d in range(4):
            if disinfect_dir[t][(d - rot)]:  # 4 방향과 방역기의 방향이 일치하는 경우
                # 해당 방향으로 방역 수행하기
                nr, nc = row, col
                while True:
                    nr += dr[d]
                    nc += dc[d]
                    # 소독약이 교실을 벗어나거나 벽을 만나면 멈춤
                    if nr < 0 or nr >= N or nc < 0 or nc >= M: break
                    if MAP[nr][nc] == 6: break
                    disinfected[nr][nc] = True

    # 방역 되지 않은 부분의 수 count
    area = sum([
        1
        for r in range(N)
        for c in range(M)
        if not disinfected[r][c] and MAP[r][c] != 6])
    return area


def get_min_area(m_idx):
    global ans
    # 종료 조건 (모든 방역기를 작동 시켰을 경우)
    if m_idx == len(MACHINE_LIST):
        # 커버되지 않은 구역의 총합 중 최솟값 업데이트
        ans = min(ans, get_area())
        return

    # 현재 방역기 정보 가져오기
    row, col, t = MACHINE_LIST[m_idx]

    # 타입 별 가능한 방역기 방향에 대해서 동작
    for rot in range(machine_can_rotate[t]):
        machine_rotated_list.append([row, col, rot, t])
        get_min_area(m_idx + 1)
        machine_rotated_list.pop()


get_min_area(0)
print(ans)