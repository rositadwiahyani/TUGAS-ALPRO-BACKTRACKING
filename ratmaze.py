

import os
import time

maze = [
    [1,1,0,0,0,1,1,1],
    [0,1,1,1,0,1,0,1],
    [0,0,0,1,0,1,0,1],
    [1,1,1,1,1,1,0,0],
    [1,0,0,0,0,1,1,1],
    [1,1,1,1,0,0,0,1],
    [0,0,0,1,1,1,0,1],
    [1,1,1,0,0,1,1,1]
]

N = len(maze)
path = [[0]*N for _ in range(N)]

START = (0, 0)
END = (N-1, N-1)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_maze():
    print("+" + "---"*N + "+")
    
    for i in range(N):
        print("|", end="")
        for j in range(N):
            if (i, j) == START:
                print(" S ", end="")
            elif (i, j) == END:
                print(" E ", end="")
            elif path[i][j] == 1:
                print(" * ", end="")
            elif maze[i][j] == 0:
                print(" █ ", end="")
            else:
                print(" . ", end="")
        print("|")
    
    print("+" + "---"*N + "+")
    print()

def is_safe(x, y):
    return 0 <= x < N and 0 <= y < N and maze[x][y] == 1 and path[x][y] == 0

def solve(x, y):
    if (x, y) == END:
        path[x][y] = 1
        clear()
        print("TUJUAN TERCAPAI!\n")
        print_maze()
        return True

    if is_safe(x, y):
        path[x][y] = 1
        clear()
        print(f"Tikus di posisi ({x},{y})")
        print_maze()
        time.sleep(0.5)

        if solve(x+1, y): return True
        if solve(x, y+1): return True
        if solve(x-1, y): return True
        if solve(x, y-1): return True

        path[x][y] = 0
        clear()
        print(f"Backtracking dari ({x},{y})")
        print_maze()
        time.sleep(1.0)

    return False


print("RAT IN A MAZE — BACKTRACKING\n")
print("S = Start | E = End | * = Jalur Tikus | █ = Tembok\n")
print_maze()
time.sleep(1)

if not solve(*START):
    print("Tidak ada jalur menuju tujuan")
