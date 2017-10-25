import random

"""Madeline Mechem, AI Project 4, Python code 2017

Code Sample for Wayfair. """

#also this breaks for very small numbers of simulations.

#q learning algorithm. q learning is a method of AI training where each possible
# outcome of a move is assigned a value based on which player it benefits.
# then, during x number of simulations, the AI plays itself using randomly generated
#moves, compiling a table of values. from there, it should be able to play itself
#or a human with little to no error. Unfortunately, it is a little bit buggy at the minute
# and keeps selecting incorrect lots to draw from.
def qlearn(simnum, start):
    qtable = {}
    for x in range(0, simnum):
        board = start
        while board != "A000"  and board != "B000":
            a, b, c, d, e, f = board
            if (int(b) == 0 and int(c) != 0 and int(d) != 0):
                pilenum = random.choice([1,2])
            elif (int(b) != 0 and int(c) == 0 and int(d) != 0):
                pilenum = random.choice([0,2])
            elif (int(b) != 0 and int(c) !=0 and int(d) == 0):
                pilenum = random.choice([0,1])
            elif (int(b) != 0 and int(c) == 0 and int(d) == 0):
                pilenum = 0
            elif (int(b) == 0 and int(c) != 0 and int(d) == 0):
                pilenum = 1
            elif (int(b) == 0 and int(c) == 0 and int(d) != 0):
                pilenum = 2
            else:
                pilenum = random.choice([0,1,2])
            list1 = list(board)
            list1[4] = str(pilenum)
            board = ''.join(list1)
            a, b, c, d, e, f = board
            if (pilenum == 0):
                sizeofpile = b
            if (pilenum == 1):
                sizeofpile = c
            if (pilenum == 2):
                sizeofpile = d
            taken = random.randint(1, int(sizeofpile))
            list2 = list(board)
            list2[5] = str(taken)
            board = ''.join(list2)
            nextstate = (board + '.')[:-1]
            a, b, c, d, e, f = nextstate
            if (pilenum == 0):
                b = str(int(b) - taken)
            if (pilenum == 1):
                c = str(int(c) - taken)
            if (pilenum == 2):
                d = str(int(d) - taken)
            if (board[0] == 'A'):
                a = 'B'
            else:
                a = 'A'
            nextstate = a + b + c  + d
            if (nextstate == 'A000'):
                reward = 1000
            elif (nextstate == 'B000'):
                reward = -1000
            else:
                reward = 0
            #print("uno\n")
            if (board[0] == 'A'):
                if board not in qtable:
                    qtable[board] = 0
                minv = 1000                
                if int(b) > 0:  
                    i = 0                   
                    while i < int(b):
                        nextstate = a + b + c + d + '1' + str((int(b)-i))
                        i += 1
                        if nextstate in qtable:
                            if minv > qtable[nextstate]:
                                minv = qtable[nextstate]                        
                if int(c) > 0:                   
                    i = 0                   
                    while i < int(c):
                        nextstate = a + b + c + d + '2' + str((int(c)-i))
                        i += 1
                        if nextstate in qtable:
                            if minv > qtable[nextstate]:
                                minv = qtable[nextstate]                
                if int(d) > 0:
                    i = 0                   
                    while i < int(d):
                        nextstate = a + b + c + d + '3' + str((int(d)-i))
                        i += 1
                        if nextstate in qtable:
                            if minv > qtable[nextstate]:
                                minv = qtable[nextstate]                            
                #print("dos\n")
                qtable[board] = (qtable[board] + (reward + float(.9*(minv)) - qtable[board]))
                board = nextstate            
            else:
                if board not in qtable:
                    qtable[board] = 0
                maxv = -1000                
                if int(b) > 0:  
                    i = 0                   
                    while i < int(b):
                        nextstate = a + b + c + d + '1' + str((int(b)-i))
                        i += 1
                        if nextstate in qtable:
                            if maxv < qtable[nextstate]:
                                maxv = qtable[nextstate]                        
                if int(c) > 0:                   
                    i = 0                   
                    while i < int(c):
                        nextstate = a + b + c + d + '2' + str((int(c)-i))
                        i += 1
                        if nextstate in qtable:
                            if maxv < qtable[nextstate]:
                                maxv = qtable[nextstate]            
                if int(d) > 0:
                    i = 0                   
                    while i < int(d):
                        nextstate = a + b + c + d + '3' + str((int(d)-i))
                        i += 1
                        if nextstate in qtable:
                            if maxv < qtable[nextstate]:
                                maxv = qtable[nextstate]                                
                qtable[board] = (qtable[board] + (reward + float(.9*(maxv)) - qtable[board]))                
                board = nextstate
    print("\nFinal Q-values:\n")
    for item in qtable:
        #print("test\n")
        print(item + " " + str(qtable[item]))
    return qtable

#my gameplay determiner. this is what actually runs the game via the rules of nim. 
def gameplay(qtable, start):
    otravez = 1
    gameplayed = 0
    while (otravez == 1):
        if (gameplayed != 0):         
            otravez = int(input("\n To play again, enter 1, or enter 9 to quit. \n"))
            if (otravez != 1):
                break
        gameplayed = 1
        board = start[:-2]
        firstplayer = int(input("\n enter 1 to move first, or 2 to let the AI move first \n"))
        if (firstplayer == 1):
            playerturn = 1
        else:
            playerturn = 2
        while board != "A000"  and board != "B000":
            if (playerturn == 1 and firstplayer == 1 or playerturn == 1 and firstplayer == 2):
                if (playerturn == 1 and firstplayer == 1):
                    currturn = 'A'
                else:
                    currturn = 'B'                  
                print("\nPlayer " + currturn + "'s turn; the board is " + board[1:])
                pilenum = (int(input("\n What pile do you chose? 1, 2, 3? \n")))-1
                while(pilenum > 2 or pilenum < 0):
                    print("\nInvalid. Pick 1, 2 or 3. \n")
                    pilenum = (int(input()))- 1
                taken = int(input("\nHow many items do you want to take? \n"))
                a, b, c, d = board
                if (pilenum == 0):
                    b = str(int(b) - taken)                 
                if (pilenum == 1):
                    c = str(int(c) - taken)
                if (pilenum == 2):
                    d = str(int(d) - taken)
                if (firstplayer == 1):
                    a = 'B'
                else:
                    a = 'A'    
                board = a + b + c + d
                if board not in qtable:
                    qtable[board] = 0
                playerturn = 2
            elif (playerturn == 2 and firstplayer == 2):
                print("\nPlayer A (AI)'s turn; board is " + board[1:]) 
           # nextboard = maxq(board, qtable)
                a, b, c, d = board
                maxqv = -1001
                if int(b) > 0:  
                    i = 0                   
                    while i < int(b):
                        nextstate = a + b + c + d + '1' + str((int(b)-i))
                        i += 1
                        if nextstate not in qtable:
                            qtable[nextstate] = 0                        
                        if (qtable[nextstate] > maxqv):
                            maxqv = qtable[nextstate]
                            nextboard = nextstate
                if int(c) > 0:                   
                    i = 0                   
                    while i < int(c):
                        nextstate = a + b + c + d + '2' + str((int(c)-i))
                        i += 1
                        if nextstate not in qtable:
                            qtable[nextstate] = 0 
                        if (qtable[nextstate] > maxqv):
                            maxqv = qtable[nextstate]
                            nextboard = nextstate        
                if int(d) > 0:
                    i = 0                   
                    while i < int(d):
                        nextstate = a + b + c + d + '3' + str((int(d)-i))
                        i += 1
                        if nextstate not in qtable:
                            qtable[nextstate] = 0 
                        if (qtable[nextstate] > maxqv):
                            maxqv = qtable[nextstate]
                            nextboard = nextstate 
                a, b, c, d, e, f = nextboard
                x, y = nextboard[4:]
                print("\nAI chooses pile " + x + " and removes " + y + ".\n")
                if (e == '2'):
                    d = int(d) - int(f)
                elif (e == '1'):
                    c = int(c) - int(f)
                elif (e == '0' ):
                    b = int(b) - int(f)
                nextboard = 'B' + str(b) + str(c) + str(d)                           
                board = nextboard
                playerturn = 1
                
            elif (playerturn == 2 and firstplayer == 1):
                print("\nPlayer B (AI)'s turn; board is " + board[1:]) 
           # nextboard = maxq(board, qtable)
                a, b, c, d = board
                minqv = 1001
                if int(b) > 0:  
                    i = 0                   
                    while i < int(b):
                        nextstate = a + b + c + d + '1' + str((int(b)-i))
                        i += 1
                        if nextstate not in qtable:
                            qtable[nextstate] = 0 
                        if (qtable[nextstate] < minqv):
                            minqv = qtable[nextstate]
                            nextboard = nextstate
                if int(c) > 0:                   
                    i = 0                   
                    while i < int(c):
                        nextstate = a + b + c + d + '2' + str((int(c)-i))
                        i += 1
                        if nextstate not in qtable:
                            qtable[nextstate] = 0 
                        if (qtable[nextstate] < minqv):
                            minqv = qtable[nextstate]
                            nextboard = nextstate        
                if int(d) > 0:
                    i = 0                   
                    while i < int(d):
                        nextstate = a + b + c + d + '3' + str((int(d)-i))
                        i += 1
                        if nextstate not in qtable:
                            qtable[nextstate] = 0 
                        if (qtable[nextstate] < minqv):
                            minqv = qtable[nextstate]
                            nextboard = nextstate 
                a, b, c, d, e, f = nextboard
                x, y = nextboard[4:]
                print("\nAI chooses pile " + x + " and removes " + y + ".\n")
                if (e == '2'):
                    d = int(d) - int(f)
                elif (e == '1'):
                    c = int(c) - int(f)
                elif (e == '0' ):
                    b = int(b) - int(f)
                nextboard = 'A' + str(b) + str(c) + str(d)                           
                board = nextboard
                playerturn = 1
        if (board == "A000"  or board == "B000"):
            print("\nGame Over.")
            if (board == "A000"):
                print("\n Player A wins!!!\n\n")
            if (board == "B000"):
                print("\n Player B wins!!!\n\n")
#main
def main():
    p1 = int(input("Welcome to Nim, with Q-Learning!\nHow many objects do you want in pile 1?\n"))
    while(p1 <0):
        p1 = int(input("Invalid Entry\nEnter new number of objects for pile 1\n"))

    p2 = int(input("How many objects do you want in pile 2?\n"))
    while(p2 <0):
        p2 = int(input("Invalid Entry\nEnter new number of objects for pile 2\n"))

    p3 = int(input("How many objects do you want in pile 3?\n"))
    while(p3 <0):
        p3 = int(input("Invalid Entry\nEnter new number of objects for pile 3\n"))

    simnum = int(input("How many games do you want to simulate? \n"))
    while(simnum <= 0):
        simnum = int(input("Invalid entry\nEnter new number that is at least 1 \n"))
    playerturn = 'A'  
    board = playerturn + str(p1) + str(p2) + str(p3) + '9' + '9'
    print("Initial board is " + str(p1) + "-" + str(p2) + "-" + str(p3) + ", simulating " + str(simnum) + " games.\n")
    qvals={}
    qvals=qlearn(simnum, board)
    gameplay(qvals, board)

main ()
