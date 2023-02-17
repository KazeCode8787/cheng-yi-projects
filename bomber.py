import random as ra

n = int(input())
bombs = int(input())
bombs_t = bombs

matrix = [[0]*n for i in range(n)]
explore = [['?']*n for i in range(n)]

# randomize the bombs
while bombs:
    x = ra.randint(0,n-1)
    y = ra.randint(0,n-1)

    if matrix[y][x] == 0:
        matrix[y][x] = 'x'
        bombs -= 1


directions = [(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1)]

# counting nearby bombs
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'x':
            continue

        for direc in directions:
            if 0<=j+direc[0]<=n-1 and 0<=i+direc[1]<=n-1 and matrix[i+direc[1]][j+direc[0]]=='x':
                matrix[i][j] += 1

# showing
def show():
    for i in range(n):
        for j in range(n):
            print(explore[i][j],end='\t')

        print()

show()


alive = True
over = False

def bfs(x,y):
    queue = [(x,y)]
    
    while queue:
        now = queue.pop(0)
        px, py = now

        for direct in directions:
            if 0<=px+direct[0]<=n-1 and 0<=py+direct[1]<=n-1:
                if matrix[py+direct[1]][px+direct[0]] == 0:
                    if explore[py+direct[1]][px+direct[0]] == '?':
                        queue.append((px+direct[0],py+direct[1]))
                        explore[py+direct[1]][px+direct[0]] = matrix[py+direct[1]][px+direct[0]]
                else:
                    explore[py+direct[1]][px+direct[0]] = matrix[py+direct[1]][px+direct[0]]


while alive and not over:
    pick_x,pick_y = map(int,input().split())

    if matrix[pick_y][pick_x] == 'x':
        alive = False

    if matrix[pick_y][pick_x] == 0:
        bfs(pick_x,pick_y)
    else:
        explore[pick_y][pick_x] = matrix[pick_y][pick_x]

    ctn = 0
    for i in range(n):
        ctn += explore[i].count('?')

    if ctn == bombs_t:
        over = True

    show()

print("Game Over!")
print(f"You {'Won' if alive else 'Lose'}")

print("Answer:")
for i in range(n):
        for j in range(n):
            print(matrix[i][j],end='\t')

        print()
