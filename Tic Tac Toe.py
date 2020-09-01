
gameboard={
    '7':' ','8':' ','9':' ',
    '4':' ','5':' ','6':' ',
    '1':' ','2':' ','3':' ' }

board_keys=[]

for key in gameboard:
    board_keys.append(key)

def showBoard(board):
    print(gameboard['7']+' | '+gameboard['8']+' | '+gameboard['9'])
    print("---------")
    print(gameboard['4']+' | '+gameboard['5']+' | '+gameboard['6'])
    print('---------')
    print(gameboard['1']+' | '+gameboard['2']+' | '+gameboard['3'])

def game():
    turn="X"
    count=0

    for i in range(10):
        showBoard(gameboard)
        move=input("It is your turn "+turn+".Which position do you choose")
        
        if gameboard[move]==' ':
            gameboard[move]=turn
            count+=1
        
        if count >= 5:
            if gameboard['7'] == gameboard['8']==gameboard['9']!=' ':
                print("Player "+turn+" Wins!!!")
                showBoard(gameboard)
                break
            elif gameboard['4'] == gameboard['5']==gameboard['6']!=' ': 
                print("Player "+turn+" Wins!!!")
                showBoard(gameboard)
                break
            elif gameboard['1'] == gameboard['2']==gameboard['3']!=' ': 
                print("Player "+turn+" Wins!!!")
                showBoard(gameboard)
                break
            elif gameboard['7'] == gameboard['4']==gameboard['1']!=' ': 
                print("Player "+turn+" Wins!!!")
                showBoard(gameboard)
                break
            elif gameboard['8'] == gameboard['5']==gameboard['2']!=' ': 
                print("Player "+turn+" Wins!!!")
                showBoard(gameboard)
                break
            elif gameboard['9'] == gameboard['6']==gameboard['3']!=' ': 
                print("Player "+turn+" Wins!!!")
                showBoard(gameboard)
                break
            elif gameboard['7'] == gameboard['5']==gameboard['3']!=' ': 
                print("Player "+turn+" Wins!!!")
                showBoard(gameboard)
                break
            elif gameboard['9'] == gameboard['5']==gameboard['1']!=' ': 
                print("Player "+turn+" Wins!!!")
                showBoard(gameboard)
                break
        if count==9:
            print("Game Over")
            print("Its a tie")
            break
        
        if turn=="X":
            turn="O"
        else:
            turn="X"

    restart=input("Do you want to play again?(Y/N)")
    if restart=="y" or restart=="Y":
        for key in board_keys:
            gameboard[key]=" "
        
        game()

game()

