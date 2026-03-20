from art import logo
import random

all_cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
user_cards=[]
computer_cards=[]  
def user_wanna_play(cards, u_cards, c_cards):
    yes_or_no = input("Do you wanna play a game of Blackjack? Type 'y' or 'n':")
    if yes_or_no == 'n':
        print("We'll take your leave. Have a nice day :)")
        return False
    if yes_or_no == 'y':
        print('\n' * 100)
        print(logo)
        u_cards.append(random.choice(cards))
        u_cards.append(random.choice(cards))
        c_cards.append(random.choice(cards))
        c_cards.append(random.choice(cards))
        user_score_evaluation(cards, u_cards, c_cards)
        return True
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        return True

def user_score_evaluation(cards, u_cards, c_cards):
    u_score = sum(u_cards)
    c_score = sum(c_cards)
    if sum(c_cards) == 21 and len(c_cards) == 2:      #computer has blackjack
        print("Your cards: ",u_cards, "Current score: ",u_score)
        print("Computer's first card:", c_cards[0])
        print("Oops! Computer has Blackjack. You lose.")
        return
    elif sum(u_cards)==21 and len(u_cards)==2:        #user has blackjack
        print("Your cards: ", u_cards, "Current score:",u_score)
        print("Computer's first card:", c_cards[0])
        print("You have Blackjack. You win! :)")
        return
    elif u_score>21:
        if 11 in u_cards:
            while u_score>21 and 11 in u_cards:
                u_cards.remove(11)
                u_cards.append(1)
                u_score=sum(u_cards)
            print("Your cards: ", u_cards, "Current score:",u_score)
            print("Computer's first card:", c_cards[0])
            if u_score>21:
                print("Oops! You went beyond 21. You Lose.")
                return
            else:
                another_card=input("Tap 'y' to get another card, tap 'n' to pass: ")
                if another_card == 'y':
                    u_cards.append(random.choice(cards))
                    user_score_evaluation(cards, u_cards, c_cards)
                else:
                    computer_score_evaluation(u_score, c_score, u_cards, c_cards, cards)
        else:
            print("Your cards: ", u_cards, "Current score:",u_score)
            print("Computer's first card:", c_cards[0])
            print("Oops! You went over 21. You Lose.")
            return
    else:
        print("Your cards: ", u_cards, "Current score:",u_score)
        print("Computer's first card:", c_cards[0])
        another_card = input("Tap 'y' to get another card tap 'n' to pass:")
        if another_card == 'y':
            u_cards.append(random.choice(cards))
            user_score_evaluation(cards, u_cards, c_cards)
        else:
            computer_score_evaluation(u_score, c_score,u_cards, c_cards, cards)

def computer_score_evaluation(u_score, c_score, u_cards, c_cards, cards):
    while c_score < 17:
        c_cards.append(random.choice(cards))
        c_score = sum(c_cards)

    print("Your final hand : ", u_cards, "Final score:", u_score)
    print("Computer's final hand : ", c_cards, "Final score:", c_score)

    if c_score > 21:
        print("Computer went over 21. You Win!")
        return
    if c_score>u_score:
        print("Computer score is greater than you. You lose.")
        return
    elif u_score>c_score:
        print("Your score is greater than Computer score. You win!")
        return
    else:
        print("It's a Draw")
        return


while True:
    user_cards.clear()
    computer_cards.clear()
    continue_game=user_wanna_play(all_cards, user_cards, computer_cards)
    if not continue_game:
        break









