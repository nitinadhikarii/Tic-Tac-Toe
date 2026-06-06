arr= [[1,2,3],[4,5,6],[7,8,9]]


class player:
    def __init__(self,name,move=None,symbol=None):
        self.name=name
        self.move = move
        self.symbol= symbol
    def statement(self):
        return f"player {self.name} has selected {self.symbol} symbol and {self.move} move"



def check_win(board,symbol):

    #checking wins for lines
    for i in range(3):

        #for rows
        if all(board[i][j] == symbol for j in range(3)):   
            return True
        
        #for columns
        if all(board[j][i] == symbol for j in range(3)):   
            return True


    #checking wins for diagonals
    if all(board[i][i] == symbol for i in range(3)):
        return True
    if all(board[i][2 - i] == symbol for i in range(3)):
        return True
    return False

def make_move(board,symbol,move):

    global counter   #counter for checking if the board is full or not/ for checking draws

    if 1 <= move <= 9:
        list_of_symbols=[p.symbol for p in [p1,p2]]
    
        #converting given move to row and column
        row= int(move-1)//3
        column = int(move-1)%3
        if board[row][column] in list_of_symbols:
                print("Invalid move! Place is already taken")
                try:
                    newmove=int(input("enter a valid move: "))
                    make_move(board,symbol,newmove)
                except ValueError:
                    print("enter a valid response") 
                
        else:
            board[row][column]=symbol
            counter+=1
    
def create_board():
    for i,e in enumerate(arr):
        print(" | ".join(str(_) for _ in e))
        if i < 2:                     
            print("--+---+--")

a=input("enter player 1 name and symbol\n(seperated by ,): ") 
p1=player((a.split(","))[0]) 
p1.symbol=(a.split(","))[1].strip()
print(p1.statement()) 
b=input("enter player 2 name and symbol\n(seperated by ,): ") 
p2=player((b.split(","))[0])
p2.symbol=(b.split(","))[1].strip()   
print(p2.statement())   


#game starts/ turn based logic
create_board()

counter=0   #counter for checking if the board is full or not/ for checking draws

while True:
    try:    
        move1= int(input("player 1 move (enter 0 to quit): "))
    except ValueError:  
        print("enter a valid response")
        continue

    if move1==0:
        break
    else:
        p1.move=move1
        print(p1.statement())
        make_move(arr,p1.symbol,move1)
        create_board()
        
        if check_win(arr,p1.symbol) == True:
            print(f"player {p1.name} has won the game with symbol {p1.symbol}")
            break
    if counter ==9:
        print("its a draw")
        break




    move2= int(input("player 2 move (enter 0 to quit): "))

    if move2==0:
        break
    else:
        p2.move=move2
        print(p2.statement())
        make_move(arr,p2.symbol,move2)
        create_board()
        if check_win(arr,p2.symbol) == True:
            print(f"player {p2.name} has won the game with symbol {p2.symbol}")
            break
    if counter ==9:
        print("its a draw")
        break