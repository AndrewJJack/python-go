# Cmput 496 sample code
# Boolean Negamax for TicTacToe
# Note that the code uses the term "success" instead of win, since it can run with
# different conditions for success. E.g. draw can also be a success.
# Written by Martin Mueller

# Update Feb 11: the printing, timing and test functionality has been moved 
# into a new file tic_tac_toe_solve_test.py .

from tic_tac_toe import TicTacToe, BLACK, WHITE, EMPTY

DRAW_WINNER = BLACK

# Success means: either a win, or toPlay is the DRAW_WINNER when its a draw
def isSuccess(state):
    global DRAW_WINNER
    color = state.winner()
    return (   color == state.toPlay 
            or (color == EMPTY and state.toPlay == DRAW_WINNER)
           )
    
def negamaxBoolean(state):
    if state.endOfGame():
        return isSuccess(state)
    for m in state.legalMoves():
        state.play(m)
        success = not negamaxBoolean(state)
        state.undoMove()
        if success:
            return True
    return False

def resultForBlack(state):
    result = negamaxBoolean(state)
    if state.toPlay == BLACK:
        return result
    else:
        return not result

def solve(state): 
    global DRAW_WINNER
    DRAW_WINNER = WHITE
    win = resultForBlack(state)
    if win:
        return BLACK
    else:
        DRAW_WINNER = BLACK
        winOrDraw = resultForBlack(state)
        if winOrDraw:
            return EMPTY
        else:
            return WHITE

