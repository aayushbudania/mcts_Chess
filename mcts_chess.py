# Team Members:-
# Bhavya Sehgal 19ucs155
# Mohammed Suraj 19ucs157
# Keshav Paliwal 19ucs158
# Aayush Prakash Budania 19ucs161

import chess
import chess.pgn
import chess.engine
import random
import time
from datetime import date
from math import log, sqrt, e, inf


class node():
    def __init__(self):
        self.state = chess.Board()
        self.action = ''
        self.children = set()
        self.parent = None
        self.N = 0
        self.n = 0
        self.v = 0


def ucb1(curr_node):
    ans = curr_node.v + 2 * (sqrt(log(curr_node.N + e + (10 ** -6)) / (curr_node.n + (10 ** -10))))
    return ans


def rollout(curr_node): # If the game is over return result else select a child node randomly.
    if curr_node.state.is_game_over():
        board = curr_node.state
        if board.result() == '1-0':
            return (1, curr_node)
        elif board.result() == '0-1':
            return (-1, curr_node)
        else:
            return (0.5, curr_node)

    all_moves = [curr_node.state.san(i) for i in list(curr_node.state.legal_moves)]
    for i in all_moves:
        temp_state = chess.Board(curr_node.state.fen())
        temp_state.push_san(i)
        child = node()
        child.state = temp_state
        child.parent = curr_node
        curr_node.children.add(child)
    random_state = random.choice(list(curr_node.children))

    return rollout(random_state)


def expansion(curr_node, isWhite): # selects the child node with max/min ucb value till we reach at leaf node
    if len(curr_node.children) == 0:
        return curr_node
    max_ucb = -inf
    if isWhite:
        max_ucb = -inf
        sel_child = None
        for i in curr_node.children:
            tmp = ucb1(i)
            if (tmp > max_ucb):
                max_ucb = tmp
                sel_child = i

        return expansion(sel_child, 0)

    else:
        min_ucb = inf
        sel_child = None
        for i in curr_node.children:
            tmp = ucb1(i)
            if (tmp < min_ucb):
                min_ucb = tmp
                sel_child = i

        return expansion(sel_child, 1)


def rollback(curr_node, reward): # backpropagates till the root node. Updates reward and visited count of each node.
    curr_node.n += 1
    curr_node.v += reward
    while curr_node.parent != None:
        curr_node.N += 1
        curr_node = curr_node.parent
    return curr_node


def mcts_pred(curr_node, over, isWhite, iterations=10):
    if over:
        return -1
    all_moves = [curr_node.state.san(i) for i in list(curr_node.state.legal_moves)]
    map_state_move = dict()

    for i in all_moves:
        tmp_state = chess.Board(curr_node.state.fen())
        tmp_state.push_san(i)
        child = node()
        child.state = tmp_state
        child.parent = curr_node
        curr_node.children.add(child)
        map_state_move[child] = i

    while iterations > 0:
        if isWhite: # White player tries to maximize the ucb value
            max_ucb = -inf
            sel_child = None
            for i in curr_node.children:
                tmp = ucb1(i)
                if tmp > max_ucb:
                    max_ucb = tmp
                    sel_child = i
            ex_child = expansion(sel_child, 0)
            reward, state = rollout(ex_child)
            curr_node = rollback(state, reward)
            iterations -= 1
        else: # Black player tries to minimize the ucb value
            min_ucb = inf
            sel_child = None
            for i in curr_node.children:
                tmp = ucb1(i)
                if tmp < min_ucb:
                    min_ucb = tmp
                    sel_child = i

            ex_child = expansion(sel_child, 1)
            reward, state = rollout(ex_child)
            curr_node = rollback(state, reward)
            iterations -= 1

    if isWhite:
        mx = -inf
        selected_move = ''
        for i in (curr_node.children):
            tmp = ucb1(i)
            if (tmp > mx):
                mx = tmp
                selected_move = map_state_move[i]
        return selected_move
    else:
        mn = inf
        selected_move = ''
        for i in (curr_node.children):
            tmp = ucb1(i)
            if (tmp < mn):
                mn = tmp
                selected_move = map_state_move[i]
        return selected_move


def setGameHeader(property, value):
    game.headers[str(property)] = str(value)


board = chess.Board()
isWhite = 1
moves = 0
pgn = []
game = chess.pgn.Game()
sm = 0
count = 0
while not board.is_game_over():
    all_moves = [board.san(i) for i in list(board.legal_moves)]
    start = time.time()
    root = node()
    root.state = board
    result = mcts_pred(root, board.is_game_over(), isWhite)
    sm+=(time.time()-start)
    board.push_san(result)
    print(result)
    print(board)
    pgn.append(result)
    isWhite ^= 1
    count+=1
    moves += 1
print()
print("Average Time for a move = ",sm/count ," Sec")
print(board)
print(" ".join(pgn))
print()
print(board.result())
setGameHeader("Event", "Chess")
setGameHeader("Site", "None")
setGameHeader("Date", date.today())
setGameHeader("Round", "1")
setGameHeader("White", "1")
setGameHeader("Black", "0")
setGameHeader("Result", board.result())
print(game)
