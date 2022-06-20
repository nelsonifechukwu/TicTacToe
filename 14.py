#bringing things together

#how to determine the winner

#handle errors

#accept player input and swap players

#aside itertools, see also how to swap between numbers

#setting the game
#refining repetitive statements 
""" 
numbers= [1 ,0]
currentnum = 0
for i in range(10):
    print (currentnum)
    currentnum = numbers[currentnum] """
import itertools


#use enumerate to access the index values of each list in the list


def win(current_game):

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
 
            return True

        else:
            return False

    #Horizontal
    for row in current_game:  
        #count returns the number of 
        # the occurence of the pecified value in a list
        #row[0], check[0], diags[0] != 0  implies that all our inputs are not zero 
        # which is an automatic win in all directions
        if all_same(row):
            print(f"Player {row[0]} is the winner -- ")
            return True

    #Vertical
    for col in range(len(current_game)): 
        check = [] 
        #count returns the number of 
        # the occurence of the pecified value in a list
        for row in current_game:
            check.append(row[col])
        if all_same(check):
            print(f"Player {check[0]} is the winner | ")
            return True


    #win_diagonally():

    #first direction to the right from the top left
    #you only win when game[0][0] == game[1][1] == game[2][2]
    diags = []
    for x in range(len(current_game)):
        diags.append(game[x][x])

    if all_same(diags):
        print(f"Player {diags[0]} is the winner /")
        return True


    diags = []
    #for enumerate, col = 0, 1, 2; reversed(range(len(game))) = 2,1,0
    #To win, game [2][0] == game [1][1] == game [0][2]
    for col, row in enumerate(reversed(range(len(current_game)))):
        diags.append(current_game[row][col])

    if all_same(diags):
        print(f"Player {diags[0]} is the winner \\")
        return True
    
    return False


def game_board(game_map, player = 0, row = 0, column = 0):
   
    #check if position is occupied
    if game_map[row][column] != 0:
        print("This position is occupied, choose another")
        return game_map
    
    print ('   0, 1, 2')
    try:
        #update the game map
        game_map[row][column] = player
        for count, row in enumerate(game):
            print (count, row)
        
        return game_map
    
    except IndexError as e:
        print("Make sure you input row/column as 0, 1 or 2", e)

play = True
players = [1,2]
while play:
    game =  [[0,0,0],
             [0,0,0], 
             [0,0,0]]

    game_won = False
    game = game_board(game)
    player_choice = itertools.cycle([1,2])
    while not game_won:
        current_player = next(player_choice) #swap between player 1 & 2
        print(f"Player is {current_player}")
        column_choice = int(input("what column do you want to play"))
        row_choice = int(input("what row do you want to play"))
        game = game_board(game, current_player, row_choice, column_choice)

    #check if game is won
    if win(game):
        game_won = True
        again = input ("Game over. Would you like to play again? (y/n)")
        if again.lower() == "y":
            print("restarting")
        elif again.lower() == "n":
            print("Bye")
            play = False
        else:
            print("Not a valid answer")
            play = False

