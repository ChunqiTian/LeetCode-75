# DFS

# 841. Keys and Rooms
def canVisitAllRooms(self, rooms):
    visited = set()
    def dfs(room):
        visited.add(room)
        for key in rooms[room]:
            if key not in visited:
                dfs(key)
    dfs(0)
    return len(visited) == len(rooms)


# 547. Number of Provinces
def findCircleNum(self, isConnected):
    n = len(isConnected)
    visited = [False] * n

    def dfs(city):
        visited[city] = True
        for neighbor in range(n):
            if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)

    provinces = 0
    for city in range(n):
        if not visited[city]:
            dfs(city)
            provinces += 1
    return provinces


# 1466. Reorder Routes to Make All Paths Lead to the City Zero
from collections import defaultdict
def minReorder(self, n, connections):
    adj = defaultdict(list)
    for u, v in connections:
        adj[u].append(v, 1)
        adj[v].append(u, 0)

    visited = set()

    def dfs(node):
        visited.add(node)
        reorder_cnt = 0
        for nei, need_reorder in adj[node]:
            if nei not in visited:
                reorder_cnt += need_reorder
                reorder_cnt += dfs(nei)
        return reorder_cnt
    return dfs(0)

# 339. Evaluate Division
# DFS Method
def calcEquation(self, equations, values, queries):
    graph = defaultdict(list)
    for (a,b), value in zip(equations, values):
        graph[a].append((b, value))
        graph[b].append((a, 1/value))
    
    def dfs(cur, target, product):
        if cur == target: return product

        visited.add(cur)

        for nei, weight in graph[cur]:
            ans = dfs(nei, target, product * weight)
            if ans != -1: return ans
        return -1
    res = []

    for start, end in queries:
        if start not in graph or end not in graph:
            res.append(-1.0)
            continue

        visited = set()
        res.append(dfs(start, end, 1))

    return res



# BFS Method
def calcEquation(self, equations, values, queries):
    
    graph = defaultdict(dict)

    for (u,v), value in zip(equations, values):
        graph[u][v] = value
        graph[v][u] = 1/value

    def bfs(start, end):
        if start not in graph or end not in graph: return -1.0
        queue = deque([(start, 1.0)])
        visited = set()

        while queue:
            current_node, current_value = queue.popleft()
            if current_node == end: return current_value
            visited.add(current_node)

            for neighbor, weight in graph[current_node].items():
                if neighbor not in visited:
                    queue.append((neighbor, current_value * weight))
        return -1.0
    results = []
    for u,v in queries: results.append(bfs(u,v))
    return results
        



#BFS

# 1926. Nearest Exit from Entrance in Maze
from collections import deque
def nearestExit(self, maze, entrance):
    rows, cols = len(maze), len(maze[0])
    queue = deque()
    queue.append((entrance[0], entrance[1], 0)) # r, c, steps
    maze[entrance[0]][entrance[1]] = "+"
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while queue:
        r, c, steps = queue.popleft()
        for dr, dc in directions:
            nr, nc = dr+r, dc+c
            if 0<=nr<rows and 0<=nc<cols and maze[nr][nc]==".": 
                if nr==0 or nr==rows-1 or nc==0 or nc==cols-1: return steps +1
                maze[nr][nc] = "+"
                queue.append((nr, nc, steps+1))
    return -1

# 994. Rotting Oranges
from collections import deque
def rottingOranges(self, grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2: queue.append((r,c))
            elif grid[r][c] == 1: fresh +=1
    
    if fresh == 0: return 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    minutes = 0

    while queue and fresh > 0:
        for _ in range(len(queue)): # track minutes
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = dr+r, dc+c
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((nr, nc))
                    fresh -= 1
        minutes += 1 # add minute when entire level finished
    if fresh > 0: return -1
    return minutes



