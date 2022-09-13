import itertools


# all lower case prefered, spacing is done using snake case
def game_board(game,player=0, row=0, column=0,just_display=False):
    try:
        if game[row][column]!=0:
            print("This position is occupied, Choose another !")
            return game,False
        if not just_display:
            game[row][column]=player
        print("   0  1  2 ")
        for count, row in enumerate(game):
            print(count,row)
            
        return game,False 
    except IndexError as e :
        print("Error : make sure you input row/between zerro and 2 ")
        return game,False
    except Exception as e:
        print("Something went wromng",e)
        return game,False

def horizontal_win(game):
    for row in game:
        if all_same(row):
            print(f"Player {row[0]} is the Winner horizontally.")
            return True

def vertical_win(game):
    for col in range(len(game)):
        check=[]
        for row in game:
            check.append(row[col])

        if all_same(check):
            print(f"Player {check[0]} is the Winner horizontally.")
            return True

def daigonal_win(game):
    diag=[]
    for col,row in enumerate(reversed(range(len(game)))):
        diag.append(game[row][col])
    if all_same(diag):
        print(f"Player {diag[0]} is the Winner diagonally.")
        return True

    diag=[]
    for ix in range(len(game)):  
        diag.append(game[ix][ix])
    if all_same(diag):
        print(f"Player {diag[0]} is the Winner diagnolly.")
        return True

def all_same(l):
    if l.count(l[0]) == len(l) and l[0]!=0:
        return True
    else:
        return False

#game[1][1]=1
# horizontal_win()
# vertical_win()
# daigonal_win()
# print(game[0][0])
# l =[1,2,3,4,5]
# print(l[1:3]) 
# first index of slice is not present, last index is present

play =True
players=[1,2]
while play:
    game= [
          [0, 0, 0],
          [0, 0, 0],
          [0, 0, 0],
          ]
    game_won =False
    game,_=game_board(game, just_display=True)
    player_choice=itertools.cycle([1,2])
    while not game_won:
        current_player=next(player_choice)
        print(f"Currest player is : {current_player}")
        played=False
        while not played:
            column_choice=int(input("what column do you want to play ? (0, 1, 2)"))
            row_choice=int(input("what row do you waat to play ? (0, 1, 2)"))
            game,played= game_board(game, current_player,row_choice,column_choice)
            if game:
                played=True
        
        if horizontal_win(game) or vertical_win(game) or daigonal_win(game):
            game_won=True
            again=input("The game is over, Would you like to play again ? (y,n)")
            if again.lower()=="y":
                print("Restartng...")
            elif again.lower()=="n":
                print("Thank you for playing")
                Play=False
            else:
                print("No a valid input, see you later")
                play=False 