import numpy as np
import Queue as queue
import copy
import csv

#Function to find blank tile (zero position)
def BlankTileLocation(StartNode):
    row = 0
    col = 0
    #For loop to check if current location is the blank tile
    for line in StartNode:
        col=0
        for n in line:
            if n==0:
                return [row,col]
            col+=1
        row+=1

#Function to move blank tile up
def up(StartNode):
    #Use blank finder funciton
    row,col = BlankTileLocation(StartNode)
    #Check if blank tile is already on the top
    if row == 0:
        return None,None
    else:
        #Copy the current node so the current node is not altered
        NewNode = copy.deepcopy(StartNode)
        #Swap blank tile and value above it
        NewNode[row][col] = NewNode[row-1][col]
        NewNode[row-1][col] = 0
        #Save the movement to get back to that location
        #so that back tracking is possible
        Move = "down"
        return NewNode, Move

#Function to move blank tile up
def down(StartNode):
    #Use blank finder funciton
    row,col = BlankTileLocation(StartNode)
    #Check if blank tile is already on the bottom
    if row == 2:
        return None,None
    else:
        #Copy the current node so the current node is not altered
        NewNode = copy.deepcopy(StartNode)
        #Swap blank tile and value above it
        NewNode[row][col] = NewNode[row+1][col]
        NewNode[row+1][col] = 0
        #Save the movement to get back to that location
        #so that back tracking is possible
        Move = "up"
        return NewNode, Move

#Function to move blank tile left
def left(StartNode):
    #Use blank finder funciton
    row,col = BlankTileLocation(StartNode)
    #Check if blank tile is already on the left
    if col == 0:
        return None,None
    else:
        #Copy the current node so the current node is not altered
        NewNode = copy.deepcopy(StartNode)
        #Swap blank tile and value above it
        NewNode[row][col] = NewNode[row][col-1]
        NewNode[row][col-1] = 0
        #Save the movement to get back to that location
        #so that back tracking is possible
        Move = "right"
        return NewNode, Move

#Function to move blank tile right
def right(StartNode):
    #Use blank finder funciton
    row,col = BlankTileLocation(StartNode)
    #Check if blank tile is already on the right
    if col == 2:
        return None,None
    else:
        #Copy the current node so the current node is not altered
        NewNode = copy.deepcopy(StartNode)
        #Swap blank tile and value above it
        NewNode[row][col] = NewNode[row][col+1]
        NewNode[row][col+1] = 0
        #Save the movement to get back to that location
        #so that back tracking is possible
        Move = "left"
        return NewNode, Move

#Function to back track moves to solution and find the optimal path
def generate_path(BackwardsNode):
    Answer = []
    NodePath = []
    NodesInfo = []

    #While loop to reverse current node until current node = StartNode
    while(BackwardsNode!=StartNode):
        #Find index of BackwardsNode in AllNodes
        I = AllNodes.index(BackwardsNode)
        x = AllMoves[I]
        #Use the index to see what move should be performed
        if (x=="left"):
            OldNode, garbage = left(BackwardsNode)
            #Stores movement in Answer
            Answer.insert(0,"right")
            #Stores Node in NodePath
            NodePath.insert(0,OldNode)
        if (x=="right"):
            OldNode, garbage = right(BackwardsNode)
            #Stores movement in Answer
            Answer.insert(0,"left")
            #Stores Node in NodePath
            NodePath.insert(0,OldNode)
        if (x=="up"):
            OldNode, garbage = up(BackwardsNode)
            #Stores movement in Answer
            Answer.insert(0,"down")
            #Stores Node in NodePath
            NodePath.insert(0,OldNode)
        if (x=="down"):
            OldNode, garbage = down(BackwardsNode)
            #Stores movement in Answer
            Answer.insert(0,"up")
            #Stores Node in NodePath
            NodePath.insert(0,OldNode)
        BackwardsNode = copy.deepcopy(OldNode);

    return NodePath, Answer


#Initalize GoalNode
GoalNode = [[[1,2,3],[4,5,6],[7,8,0]]]
#Input StartNode
row1 = [int(input('Enter puzzle values left to right and press enter after each number \n')),int(input()),int(input())]
row2 = [int(input()),int(input()),int(input())]
row3 = [int(input()),int(input()),int(input())]
StartNode = [row1,row2,row3]
AllMoves = ["Start"]
AllNodes = []
AllNodes.append(StartNode)

#Initalize queue
Q = queue.Queue()
Q.put(StartNode)
Visited = []
NodesInfo = []
sol = 0 #solution not found

count = 0
count2 = 0
#While loop to perform movements and save nodes until GoalNode is reached
while(Q.qsize()!=0) and (sol != 1):
    CurrentNode = Q.get()
    Visited.append(CurrentNode)
    #Perform each movie if able

    for move in [up,down,left,right]:
        NewNode, Move = move(CurrentNode)
        #If there is a NewNode, then...
        if NewNode:
            #If NewNode is not in Visited yet...
            if NewNode not in Visited:
                #Add node and movement to list
                AllNodes.append(NewNode)
                AllMoves.append(Move)
                count2+=1
                #Save current node and parent node
                NodesInfo.append([(count2),count])
                #If NewNode = GoalNode, then finished
                if NewNode in GoalNode:
                    print("FINISHED!!!")
                    sol = 1 #solution found
                else:
                    #If not finished, put NewNode in queue
                    Q.put(NewNode)
    #Print count ever 1000 iterations
    count+=1
    if(count%1000==0):
        print(count)

#Perform back tracking with desired node BackwardsNode
BackwardsNode = [[1,2,3],[4,5,6],[7,8,0]]
NodePath, Answer = generate_path(BackwardsNode)
print(Answer)
#Write NodePath to a text file
with open("nodePath.txt","wb") as f:
    w = csv.writer(f,delimiter='\n',lineterminator='\n\r\n')
    w.writerows(NodePath)
#Write NodePath to a text file
with open("Nodes.txt","wb") as f:
    w = csv.writer(f,delimiter='\n',lineterminator='\n\r\n')
    w.writerows(Visited)
#Write NodesInfo to a text file
with open("NodesInfo.txt","wb") as f:
    w = csv.writer(f,lineterminator='\n')
    w.writerows(NodesInfo)
#Write Directions to text file
with open("Optimal_Path_Directions.txt","wb") as f:
    w = csv.writer(f,lineterminator='\n')
    w.writerows(Answer)
