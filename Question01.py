import math
import sys
sys.stdin = open("answer.txt")

n = int(input())
nums = list(map(int, input().split()))

reply = list(map(int, input().split())) # + - * //
opers = []
opers_TF = [False]*(n-1)
max_val, min_val = -math.inf, math.inf
for i in range(4):
    for _ in range(reply[i]):
        opers.append(i)

def operation(x, y, o):
    if oper == 0: return a + b 
    if oper == 1: return a - b
    if oper == 2: return a * b
    if oper == 3:
        if a < 0:
            return - (abs(a) // b)
        else: return a // b

def sol(res, nums_idx):
    global max_val, min_val

    if nums_idx == n:
        max_val = max([res, max_val])
        min_val = min([res, min_val])
        return

    for idx, oper in enumerate(opers):
        if not opers_TF[idx]:
            opers_TF[idx] = True
            sol(operation(res, nums[nums_idx], oper), nums_idx+1)
            opers_TF[idx] = False

sol(nums[0], 1)
print(max_val, min_val)
