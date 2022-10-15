from math import inf

def minimax(depth, board, play, AI): 
    if len(board.get_empty()) == 0 or board.check_winner()[0]:
        return ((-1,-1), evaluate(board, board.AI), depth)
    
    if play == 'X': #make sure next play alternates between X,O
        new_play = 'O'
    else:
        new_play = 'X'
    
    if AI:
        best = ((-1,-1), -inf, depth)
    else:
        best = ((-1,-1), inf, depth)
    
    for pos in board.get_empty():
        board.update_board(pos, play)
        score = minimax(depth+1, board, new_play, not AI)
        board.update_board(pos, None)
        score = (pos, score[1], score[2])
        
        if AI and (score[1] > best[1] or (score[1] == best[1] and score[2] < best[2])):
            best = score
        elif not AI and (score[1] < best[1]) or (score[1] == best[1] and score[2] < best[2]):
            best = score

    return best

def evaluate(board, play):
    score = board.check_winner()
    if not score[0]:
        return 0
    elif play == score[1]:
        return 10
    else:
        return -10