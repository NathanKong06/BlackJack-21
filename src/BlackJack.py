import random
import sys

def blackjack(value):
    if int(value) == int(21):
        return True
    return False
    
def bust(value):
    if int(value) > int(21):
        return True
    return False
    
def card_conversion(card,full_string):
    if card == '1' and full_string[1] == '0':
        return 10
    elif card == 'A':
        return 11
    elif card in {'J','Q','K'}:
        return 10
    else:
        return int(card)
        
def hit(value,deck):
    new_card = deck[0][0]
    converted_card = card_conversion(new_card,deck[0])
    print("New card:",deck[0])
    return (int(value) + converted_card)
    
def main():
    dealer_blackjack = False
    user_blackjack = False
    dealer_ace = False
    user_ace = False
    
    full_deck = ["Ace of Spades","Ace of Hearts","Ace of Diamonds","Ace of Clubs","2 of Spades","2 of Hearts","2 of Diamonds","2 of Clubs","3 of Spades","3 of Hearts","3 of Diamonds","3 of Clubs","4 of Spades","4 of Hearts","4 of Diamonds","4 of Clubs","5 of Spades","5 of Hearts","5 of Diamonds","5 of Clubs","6 of Spades","6 of Hearts","6 of Diamonds","6 of Clubs","7 of Spades","7 of Hearts","7 of Diamonds","7 of Clubs","8 of Spades","8 of Hearts","8 of Diamonds","8 of Clubs","9 of Spades","9 of Hearts","9 of Diamonds","9 of Clubs","10 of Spades",    "10 of Hearts","10 of Diamonds","10 of Clubs","J of Spades","J of Hearts","J of Diamonds","J of Clubs","Q of Spades","Q of Hearts","Q of Diamonds","Q of Clubs","K of Spades","K of Hearts","K of Diamonds","K of Clubs"]
    random.shuffle(full_deck)
    random.shuffle(full_deck)

    print("Dealer hand:")
    print("Hidden")
    print(full_deck[1],"\n")
    dealer_temp1 = full_deck[0]
    dealer_temp2 = full_deck[1]
    first_card = card_conversion(full_deck[0][0], full_deck[0])
    second_card = card_conversion(full_deck[1][0], full_deck[1])
    full_deck.pop(0)
    full_deck.pop(0)
    combined = first_card + second_card
    if first_card == 11 or second_card == 11:
        dealer_ace = True
    if blackjack(combined):
        dealer_blackjack = True
    if bust(combined):
        combined = 12
        dealer_ace = True
    
    print("Your hand:")
    print(full_deck[0])
    print(full_deck[1])
    user_first_card = card_conversion(full_deck[0][0],full_deck[0])
    user_second_card = card_conversion(full_deck[1][0],full_deck[1])
    full_deck.pop(0)
    full_deck.pop(0)
    if user_first_card == 11 or user_second_card == 11:
        user_ace = True
    user_combined = user_first_card + user_second_card
    print("Current value in hand:", user_combined)
    if blackjack(user_combined):
        user_blackjack = True
    if bust(user_combined):
        user_combined = 12
        user_ace = True
        
    if user_blackjack and dealer_blackjack:
        print("Push! Both have blackjack!")
        sys.exit()
    elif user_blackjack and not dealer_blackjack:
        print("You win by blackjack!")
        sys.exit()
    elif not user_blackjack and dealer_blackjack:
        print("Dealer wins by blackjack!")
        sys.exit()

    
    if blackjack(user_combined):
        user_blackjack = True
    elif bust(user_combined):
        print("Current value in hand:", user_combined)
        print("You have busted. You lose.")
        sys.exit()
    else:
        user_input = input("Do you want to hit? Enter [Y/N] ")
        while user_input not in {"y","Y","n","N"} :
            user_input = input("Try again. Invalid input. [Y/N] ")
        while user_input not in {"n","N"}:
            if user_input in {"y","Y"}:
                past_user_combined = user_combined
                user_combined = hit(user_combined,full_deck)
                if (user_combined - past_user_combined) == 11 and user_ace:
                    user_combined = user_combined - 10
                elif (user_combined - past_user_combined) == 11 and not user_ace:
                    user_ace = True
                elif (user_combined - past_user_combined) == 11 and not user_ace and bust(user_combined):
                    user_combined = user_combined - 10
                    user_ace = True
                elif (user_combined - past_user_combined) == 11 and not user_ace and not bust(user_combined):
                    user_ace = True
                if bust(user_combined) and user_ace:
                    user_combined = user_combined - 10
                if bust(user_combined):
                    print("Current value in hand:", user_combined)
                    print("You have busted. You lose.")
                    sys.exit()
                elif blackjack(user_combined):
                    print("You have 21.")
                    break
                full_deck.pop(0)
                print("Current value in hand:", user_combined)
                user_input = input("Hit again? [Y/N] ")
                while user_input not in {"y","Y","n","N"} :
                    user_input = input("Try again. Invalid input. [Y/N]")
    print("Your hand value:",user_combined,"\n")
            
    
    print("Dealer hand: ")
    print(dealer_temp1)
    print(dealer_temp2)
    print("Current value in dealer hand: ", combined)
    
    if blackjack(combined):
        dealer_blackjack = True
    elif bust(combined):
        print("Current value in dealer hand: ", combined)
        print("Dealer has busted. You win!")
        sys.exit()
    else:
        while(combined < 17):
            print("Dealer hits.")
            previous_combined = combined
            combined = hit(combined,full_deck)
            if (combined - previous_combined) == 11 and dealer_ace:
                combined = combined - 10
            elif (combined - previous_combined) == 11 and not dealer_ace:
                dealer_ace = True
            elif (combined - previous_combined) == 11 and not dealer_ace and bust(combined):
                combined = combined - 10
                dealer_ace = True
            elif (combined - previous_combined) == 11 and not dealer_ace and not bust(combined):
                dealer_ace = True
            if bust(combined) and dealer_ace:
                combined = combined - 10
            print("Current value in dealer hand: ", combined)
            full_deck.pop(0)

    if bust(combined):
        print("Dealer has busted. You win!")
        sys.exit()
    elif blackjack(combined):
        dealer_blackjack = True
    else:
        print("Dealer hand final value:")
        print(combined)
        
    if (dealer_blackjack and user_blackjack) or (combined  == user_combined):
        print("Push!")
    elif (user_combined > combined):
        print("You win!")
    else:
        print("Dealer wins!")
    
    
if __name__ == "__main__":
    main()