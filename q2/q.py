# # Possible movement = -17 || -15 || -10 || -6 || +6 || +10 || +15 || +17
# POSSIBLE_MOVES = [-17, -15, -10, -6, 6, 10, 15, 17]

# def solution_recurse(current_pos, dest, distances, moves):
#     # If the number of moves made exceeds the maximum possible for a knight on 
#     # a chess board from any position to another, the path is infeasible
#     if moves > 6:
#         return float('inf')
    
#     # If the destination is reached, return the number of moves to get there
#     if current_pos == dest:
#         return moves
    
#     # # If the current position has already been visited, return the moves from here
#     # if distances[current_pos] != float('inf'):
#     #     return distances[current_pos]

#     current_moves = []
#     for move in POSSIBLE_MOVES:
#         current_move = current_pos + move

#         # Skip if the current move being made falls off the chess board
#         if current_move < 0 or current_move > 63:
#             continue

#         current_moves.append(solution_recurse(current_move, dest, distances, moves+1))
    
#     return min(current_moves)

# def solution(src, dest):
#     if src == dest:
#         return 0
#     distances = [float('inf')] * 64
#     return solution_recurse(src, dest, distances, 0)

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
   
# -2 -1 || -2 +1 || -1 -2 || -1 +2 || +1 -2 || +1 +2 || +2 -1 || +2 +1
POSSIBLE_MOVES = [Vector2D(-2, -1), Vector2D(-2, 1), Vector2D(-1, -2), Vector2D(-1, 2), Vector2D(1, -2), Vector2D(1, 2), Vector2D(2, -1), Vector2D(2, 1)]

def solution_recursive(board, memo, pos, dest, moves):
    if moves > 6:
        return float('inf')
    if pos.x == dest.x and pos.y == dest.y:
        return moves
    if memo[pos.x][pos.y] != float('inf'):
        return memo[pos.x][pos.y]

    current_moves = []
    for move in POSSIBLE_MOVES:
        current_x = pos.x + move.x
        current_y = pos.y + move.y
        if current_x >= 0 and current_x <= 7 and current_y >= 0 and current_y <= 7:
            current_move = Vector2D(current_x, current_y)
            result = solution_recursive(board, memo, current_move, dest, moves+1)
            current_moves.append(result)
    memo[pos.x][pos.y] = min(current_moves)
    return memo[pos.x][pos.y]

def solution(src, dest):
    if src == dest:
        return 0
    
    # 2D array representing the chess board
    board = []
    for i in range(64):
        if i % 8 == 0:
            board.append([i])
        else:
            board[i // 8].append(i)
    
    # Conversion to 2D
    source = Vector2D(board[src // 8].index(src), src // 8)
    destination = Vector2D(board[dest // 8].index(dest), dest // 8)

    memo = [[float('inf')] * 8 for _ in range(8)]

    return solution_recursive(board, memo, source, destination, 0)


# driver
if __name__ == '__main__':
    ex1 = solution(0, 1)
    print(ex1)
    print(ex1 == 3)
    
    ex2 = solution(19, 36)
    print(ex2)
    print(ex2 == 1)

    ex3 = solution(0, 63)
    print(ex3)

    ex4 = solution(0, 62)
    print(ex4)
    
    ex5 = solution(0, 0)
    print(ex5)