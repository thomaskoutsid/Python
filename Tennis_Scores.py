'''
Thomas Koutsidis
June 25th, 2022

Question 5

This program has a function point() which prompts the user for a player who wins a point and returns "A" if player A wins, and "B" is player B wins, or "Q" is the user quits.
The function game() keeps score of the game and prints a winner.
The function display() prints the current score in accordance with tennis rules for a game.
The function main() calls the function game().
This game replicates a sport with two players. A winner is crowned when a player has at least 4 points and wins by at least 2 points. 
'''

def point():
    point = input("Who wins a point, player A or player B? ")
    if point.upper() == "A":
        return "A"
    if point.upper() == "B":
        return "B"
    if point.upper() == "Q":
        return "Q"
    if point.upper() != ["ABQ"]:
        return "E"


def game():
    a_score = 0
    b_score = 0
    
    while True:
        score = point()
        
        if score == "A":
            a_score += 1
        elif score == "B":
            b_score += 1 
        elif score == "Q":
            print("You quit the game.")
            break
        elif score != ["ABQ"]:
            print("Invalid input. Please enter A, B or Q (to quit).")
        
        if (a_score >= 4 and a_score - b_score >= 2):
            print("Player A wins the game.")
            return
        elif (b_score >= 4 and b_score - a_score >= 2):
            print("Player B wins the game.")
            return
           
        else:
            display(a_score, b_score)

  
def display(a_score, b_score):
    a = ""
    b = ""
    if (a_score >= 3) and (b_score >= 3):
        if a_score > b_score:
            a = "Adv"
        elif b_score > a_score:
            b = "Adv"
        else:
            a = "40"
            b = "40"
    else:
        tennis = [0, 15, 30, 40]
        if a_score == 0:
            a = tennis[0]
        elif a_score == 1:
            a = tennis[1]
        elif a_score == 2:
            a = tennis[2]
        else:
            a = tennis[3]
        if b_score == 0:
            b = tennis[0]
        elif b_score == 1:
            b = tennis[1]
        elif b_score == 2:
            b = tennis[2]
        else:
            b = tennis[3]
            
    print("Score of Player A:", a)
    print("Score of Player B:", b)
            

def main():
    game()
    

main()
    
        

        
