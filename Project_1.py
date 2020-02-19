import numpy as np
import queue

GoalState = [1, 2, 3, 4, 5, 6, 7, 8, 0]
GoalNode = np.array((1, 2, 3, 4, 5, 6, 7, 8, 0)).reshape(3,3)

initial_state = [[1,2,0,3,4,5,6,7,8]]
initial_array = np.array(initial_state).reshape(3,3)
AllMoves = ("Start")
AllNodes = []
np.append(AllNodes,initial_state)
np.append(AllNodes,initial_state)
print(AllNodes)

def BlankTileLocation(initial_array):
    row,col = np.where(initial_array == 0)
    return (row,col)

def down(initial_array, row, col):
    if row == 2:
        return None
    else:
        NewNode = initial_array
        NewNode[row,col] = NewNode[row+1,col]
        NewNode[row+1,col] = 0
        Move = "down"
        return NewNode, Move

def up(initial_array, row, col):
    if row == 0:
        return None
    else:
        NewNode = initial_array
        NewNode[row,col] = NewNode[row-1,col]
        NewNode[row-1,col] = 0
        Move = "up"
        return NewNode, Move

def right(initial_array, row, col):
    if col == 2:
        return None
    else:
        NewNode = initial_array
        NewNode[row,col] = NewNode[row,col+1]
        NewNode[row,col+1] = 0
        Move = "right"
        return NewNode, Move

def left(initial_array, row, col):
    if col == 0:
        return None
    else:
        NewNode = initial_array
        NewNode[row,col] = NewNode[row,col-1]
        NewNode[row,col-1] = 0
        Move = "left"
        return NewNode, Move

def AddNode(NewNode):
    np.vstack(AllMoves,Move)

    if NewNode in AllNodes:
        np.vstack(AllNodes,NewNode)
        return AllMoves,AllNodes
    else:
        np.vstack(Nodes,NewNode)
        np.vstack(AllNodes,NewNode)
        return Nodes,AllMoves,AllNodes

def CheckGoal(NewNode):
    if NewNode == GoalNode:
        Finish = 1
        return Finish



row,col = BlankTileLocation(initial_array)
NewNode, Move = up(initial_array, row, col)
print(NewNode)
#
# #while not finished
# row,col = BlankTileLocation(initial_array)
# NewNode, Move = down(initial_array, row, col)
# if down is not None:
#     print(NewNode)
#     #check if in allnodes
#     #if not
#         #add to queue
#         #add move
# NewNode, Move = up(initial_array, row, col)
# if up is not None:
#     print(NewNode)
# NewNode, Move = right(initial_array, row, col)
# if right is not None:
#     print(NewNode)
# NewNode, Move = left(initial_array, row, col)
# if left is not None:
#     print(NewNode)

# res = any(np.array_equal(Test, i) for i in Nodes)
# print(res)
# if Test in GoalNode:
#     # np.append(Nodes,NewNode)
#     print("TES")
