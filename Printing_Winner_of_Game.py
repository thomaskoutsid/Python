'''
Thomas Koutsidis
June 18th, 2022

Question 4

The function point() prompts the user for a player who wins and returns "A" if player A wins a point and "B" if player B wins a point.
The function game() keeps the score in the game and returns "A" if player A wins the game or "B" if player B wins the game.
The function main() calls the previous functions and prints the winner of the game.
'''

def point():
    player = input("Who wins the point, player A or B? ")
    if player.upper() == "A":
        return "A"
    if player.upper() == "B":
        return "B"
    else:
        print("Invalid input.")
        return "E"


def game():
    a_score = 0
    b_score = 0
    
    for i in range(13):
      player_score = point()
    
      if player_score == "A":
        a_score = a_score + 1
      elif player_score == "B":
        b_score = b_score + 1
        
      print("A score: ", a_score)
      print("B score: ", b_score)
   
      if (a_score >= 3) and (a_score - b_score >= 2):
        return "A"
      elif (b_score >= 3) and (b_score - a_score >= 2):
        return "B"
      elif (a_score >= 7) and (a_score > b_score):
        return "A"
      elif (b_score >= 7) and (b_score > a_score):
        return "B"
    

def main():
    print("This program keeps the score of a game.")
    winner = game()
    print("The winner is player", winner)
    
    
main()
