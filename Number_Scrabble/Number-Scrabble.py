# File : CS112_A1_T2_2_20230231
# Purpose : Number scrabble involves players picking numbers from a list of 1-9
#           with the winner picking three numbers that add up to 15,
#           and the game ends if all numbers are used
# Author: Abdallah Mohammed Abdallah
# ID: 20230231



def check_the_winner(numbers): #function  to check which player wins
    return sum(numbers) == 15

def check_the_draw(player1_list, player2_list): # function to check the draw

    all_numbers = set(range(1, 9))
    used_numbers = set(player1_list + player2_list) #we check if the all numbers has been choosen
    return all_numbers == used_numbers




def main ():
    print("** Welcome to Number Scrabble **")
    game_list=[1,2,3,4,5,6,7,8,9] # the set of numbers
    player1_list=[]
    player2_list=[]
    while True :
        player1_input=int(input("Player 1 choose a number :"))

        if player1_input in game_list  : # to check validation

            player1_list.append(player1_input)# to add the number to player 1 's list
            game_list.remove(player1_input) #to remove the number from game_list
            print("player 1 numbers are : ", player1_list)
            print("The remaining numbers are : ", game_list)


        else : #if player 1 choose a not valid number
            player1_input=int(input("Invalid, please choose a valid number :"))#let player 1 to choose again
            player1_list.append(player1_input) #to add the number to player 1 's list
            game_list.remove(player1_input) #to remove the number from game_list
            print("player 1 numbers are : ", player1_list)
            print("The remaining numbers are : ", game_list)

        player2_input = int(input("Player 2 choose a number"))

        if player2_input in game_list : # to check validation

            player2_list.append(player2_input)#to add the number to player 2 's list
            game_list.remove(player2_input) #to remove the number from game_list
            print("player 2 numbers are : ", player2_list)
            print("The remaining numbers are : ", game_list)

        else :#if player 2 choose a not valid number
            player2_input= int(input("Invalid, please choose a valid number :"))
            player2_list.append(player2_input)#to add the number to player 2 's list
            game_list.remove(player2_input)#to add the number to player 2 's list
            print("player 2 numbers are : ", player2_list)
            print("The remaining numbers are : ", game_list)

        if check_the_winner(player1_list):
            print("Player 1 wins!")
            exit()
        elif check_the_winner(player2_list):
            print("Player 2 wins!")
            exit()
        elif check_the_draw(player1_list, player2_list):
            print("It's a draw!")
            exit()


if __name__ == "__main__":
    main()