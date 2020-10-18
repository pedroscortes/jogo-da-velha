import uuid
from random import randint

theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in theBoard:
    board_keys.append(key)

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def game():

    turn = 'X'

count = 0

firstPlayer = randint(1, 2)
if firstPlayer == 1:
    turn = 'X'
elif firstPlayer == 2:
    turn = 'O'   


id = uuid.uuid4()


print ("O id da partida é: ",end="")
print(id)  


for i in range(10):
    printBoard(theBoard)
    print("É sua vez, " + turn + ". Aonde deseja jogar?")

    move = input()        

    if theBoard[move] == ' ':
        theBoard[move] = turn
        count += 1
    else:
        print("Este campo já esta preenchido!.\nAonde deseja jogar?")
        continue

        
    if count >= 5:
        if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
            printBoard(theBoard)
            print("\nPartida Finalizada.\n")                
            print("O jogador " +turn + " venceu.")                
            break
        elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
            printBoard(theBoard)
            print("\nGame Over.\n")                
            print("O jogador " +turn + " venceu.")
            break
        elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
            printBoard(theBoard)
            print("\nPartida Finalizada.\n")                
            print("O jogador " +turn + " venceu.")
            break
        elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
            printBoard(theBoard)
            print("\nPartida Finalizada.\n")                
            print("O jogador " +turn + " venceu.")
            break
        elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
            printBoard(theBoard)
            print("\nPartida Finalizada.\n")                
            print("O jogador " +turn + " venceu.")
            break
        elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
            printBoard(theBoard)
            print("\nPartida Finalizada.\n")                
            print("O jogador " +turn + " venceu.")
            break 
        elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
            printBoard(theBoard)
            print("\nPartida Finalizada.\n")                
            print("O jogador " +turn + " venceu.")
            break
        elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
            printBoard(theBoard)
            print("\nPartida Finalizada.\n")                
            print("O jogador " +turn + " venceu.")
            break 

        
    if count == 9:
        print("\nPartida Finalizada.\n")                
        print("O jogo empatou!")
        break

        
    if turn =='X':
        turn = 'O'
    else:
        turn = 'X'        
    
    game()