import sys

M, N, K = map(int, sys.stdin.readline().split())

table = [[0 for i in range(N)] for j in range(M)]

for i in range(K):
    s_x, s_y, e_x, e_y = map(int, sys.stdin.readline().split())

    for m in range(s_y, e_y):
        for j in range(s_x, e_x):
            table[m][j] = 1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
count_arr = []

for i in range(M):
    for j in range(N):
        if table[i][j] == 0:
            count = 1
            table[i][j] = 1
            queue = [[i, j]]

            while queue:
                x, y = queue[0][0], queue[0][1]
                del queue[0]
                for t in range(4):
                    new_x = x + dx[t]
                    new_y = y + dy[t]
                    if 0 <= new_x < M and 0 <= new_y < N and table[new_x][new_y] == 0:
                        count += 1
                        table[new_x][new_y] = 1
                        queue.append([new_x, new_y])
            count_arr.append(count)

count_arr=sorted(count_arr)
print(len(count_arr))
for i in count_arr:
    print(i, end=' ')

