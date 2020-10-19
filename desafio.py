import uuid
from random import randint

theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

boardKeys = []

for key in theBoard:
    boardKeys.append(key)

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


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
        if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
            printBoard(theBoard)
            print("\nPartida Finalizada.\n")                
            print("O jogador " +turn + " venceu.")                
            break
        elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': 
            printBoard(theBoard)
            print("\nGame Over.\n")                
            print("O jogador " +turn + " venceu.")
            break
        elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':  
            printBoard(theBoard)
            print("\nPartida Finalizada.\n")                
            print("O jogador " +turn + " venceu.")
            break
        elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':  
            printBoard(theBoard)
            print("\nPartida Finalizada.\n")                
            print("O jogador " +turn + " venceu.")
            break
        elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': 
            printBoard(theBoard)
            print("\nPartida Finalizada.\n")                
            print("O jogador " +turn + " venceu.")
            break
        elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': 
            printBoard(theBoard)
            print("\nPartida Finalizada.\n")                
            print("O jogador " +turn + " venceu.")
            break 
        elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': 
            printBoard(theBoard)
            print("\nPartida Finalizada.\n")                
            print("O jogador " +turn + " venceu.")
            break
        elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': 
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
