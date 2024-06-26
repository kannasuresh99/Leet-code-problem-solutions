from collections import deque

def bfs(arr, start, end):
    rows, cols = len(arr), len(arr[0])
    visited = [[False] * cols for _ in range(rows)]
    queue = deque([(start[0], start[1], 0)])
    
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        current_row, current_col, min_val = queue.popleft()
        
        if (current_row, current_col) == end:
            return min_val

        for move in moves:
            new_row, new_col = current_row + move[0], current_col + move[1]

            if 0 <= new_row < rows and 0 <= new_col < cols and not visited[new_row][new_col]:
                new_min_val = min(min_val, arr[new_row][new_col])
                queue.append((new_row, new_col, new_min_val))
                visited[new_row][new_col] = True

    return -1  # Return -1 if no valid path is found

# Example usage
arr = [
    [0, 0, 0, 0, 0],
    [1, 9, 9, 9, 1],
    [0, 0, 0, 0, 0]
]

start_point = (0, 3)
end_point = (2, 3)

result = bfs(arr, start_point, end_point)
print(result)
