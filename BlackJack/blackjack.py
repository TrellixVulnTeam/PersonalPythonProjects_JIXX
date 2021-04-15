import random

money = 100
deck = ["2H", "3h", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH", "AH", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC", "AC", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS", "AS", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD", "AD"]
#random.shuffle(deck)

print("************\n"
      "*Black Jack*\n"
      "************\n")

def calculate(card1, card2 = "0", card3 = "0", card4 = "0", card5 = "0", card6 = "0", card7 = "0", card8 = "0", card9 = "0", card10 = "0", card11 = "0"):
    card1Val = 0
    card2Val = 0
    card3Val = 0
    card4Val = 0
    card5Val = 0
    card6Val = 0
    card7Val = 0
    card8Val = 0
    card9Val = 0
    card10Val = 0
    card11Val = 0

    if card1[0] == "1" or card1[0] =="J" or card1[0] == "Q" or card1[0] == "K":
        card1Val = 10
    elif card1[0] == "A":
        card1Val = 11
    else:
        card1Val = int(card1[0])

    if card2[0] == "1" or card2[0] == "J" or card2[0] == "Q" or card2[0] == "K":
        card2Val = 10
    elif card2[0] == "A":
        card2Val = 11
    else:
        card2Val = int(card2[0])
        
    if card3[0] == "1" or card3[0] == "J" or card3[0] == "Q" or card3[0] == "K":
        card3Val = 10
    elif card3[0] == "A":
        card3Val = 11
    else:
        card3Val = int(card3[0])
        
    if card4[0] == "1" or card4[0] == "J" or card4[0] == "Q" or card4[0] == "K":
        card4Val = 10
    elif card4[0] == "A":
        card4Val = 11
    else:
        card4Val = int(card4[0])
    
    if card5[0] == "1" or card5[0] == "J" or card5[0] == "Q" or card5[0] == "K":
        card5Val = 10
    elif card5[0] == "A":
        card5Val = 11
    else:
        card5Val = int(card5[0])
        
    if card6[0] == "1" or card6[0] == "J" or card6[0] == "Q" or card6[0] == "K":
        card6Val = 10
    elif card6[0] == "A":
        card6Val = 11
    else:
        card6Val = int(card6[0])
        
    if card7[0] == "1" or card7[0] == "J" or card7[0] == "Q" or card7[0] == "K":
        card7Val = 10
    elif card7[0] == "A":
        card7Val = 11
    else:
        card7Val = int(card7[0])
        
    if card8[0] == "1" or card8[0] == "J" or card8[0] == "Q" or card8[0] == "K":
        card8Val = 10
    elif card8[0] == "A":
        card8Val = 11
    else:
        card8Val = int(card8[0])
        
    if card9[0] == "1" or card9[0] == "J" or card9[0] == "Q" or card9[0] == "K":
        card9Val = 10
    elif card9[0] == "A":
        card9Val = 11
    else:
        card9Val = int(card9[0])
        
    if card10[0] == "1" or card10[0] == "J" or card10[0] == "Q" or card10[0] == "K":
        card10Val = 10
    elif card10[0] == "A":
        card10Val = 11
    else:
        card10Val = int(card10[0])
        
    if card11[0] == "1" or card11[0] == "J" or card11[0] == "Q" or card11[0] == "K":
        card11Val = 10
    elif card11[0] == "A":
        card11Val = 11
    else:
        card11Val = int(card11[0])


    return card1Val + card2Val + card3Val + card4Val + card5Val + card6Val + card7Val + card8Val + card9Val + card10Val + card11Val


while True:
    bet = int(input("Your account balance is " + str(money) + " dollars. How much would you like to bet? >>> "))
    if bet > money:
        print("You don't have that much money!")
        continue
    if bet == 69:
        print("Nice.")
    if bet == 420:
        print("Blaze it.")

    random.shuffle(deck)

    dealerVal = calculate(deck[51])
    playerVal = calculate(deck[0], deck[1])
    print("Your cards are: " + deck[0] + " and " + deck[1] + " which add up to " + str(playerVal))
    print("Dealer's visible card is: " + deck[51] + " which is worth " + str(dealerVal))
    ans = input("Would you like to hit? y/n >>> ")
    if ans == "y":
        print("1 hit")
        playerVal = calculate(deck[0], deck[1], deck[2])
        print("Your cards are: " + deck[0] + ", " + deck[1] + ", and " + deck[2] + " which add up to " + str(playerVal))
        print("Dealer's visible card is: " + deck[51] + " which is worth " + str(dealerVal))
        ans = input("Would you like to hit? y/n >>> ") #I know this is a god awful way of doing this but it should work. In theory it's possible to hit 9 times
        if ans == "y":
            print("2 hit")
            playerVal = calculate(deck[0], deck[1], deck[2], deck[3])
            print("Your cards are: " + deck[0] + ", " + deck[1] + ", " + deck[2] + " , and " + deck[3] + " which add up to " + str(playerVal))
            print("Dealer's visible card is: " + deck[51] + " which is worth " + str(dealerVal))
            ans = input("Would you like to hit? y/n >>> ")
            if ans == "y":
                print("3 hit")
                playerVal = calculate(deck[0], deck[1], deck[2], deck[3], deck[4])
                print("Your cards are: " + deck[0] + ", " + deck[1] + ", " + deck[2] + ", " + deck[3] + ", and " + deck[
                    4] + " which add up to " + str(playerVal))
                print("Dealer's visible card is: " + deck[51] + " which is worth " + str(dealerVal))
                ans = input("Would you like to hit? y/n >>> ")
                if ans == "y":
                    print("4 hit")
                    playerVal = calculate(deck[0], deck[1], deck[2], deck[3], deck[4], deck[5])
                    print("Your cards are: " + deck[0] + ", " + deck[1] + ", " + deck[2] + ", " + deck[3] + ", " + deck[4] + ", and " +
                          deck[5] + " which add up to " + str(playerVal))
                    print("Dealer's visible card is: " + deck[51] + " which is worth " + str(dealerVal))
                    ans = input("Would you like to hit? y/n >>> ")
                    if ans == "y":
                        print("5 hit")
                        ans = input("Would you like to hit? y/n >>> ") #oh it just keeps going
                        if ans == "y":
                            print("6 hit")
                            ans = input("Would you like to hit? y/n >>> ")
                            if ans == "y":
                                print("7 hit")
                                ans = input("Would you like to hit? y/n >>> ")
                                if ans == "y":
                                    print("8 hit")
                                    ans = input("Would you like to hit? y/n >>> ")
                                    if ans == "y":
                                        print("9 hit")


