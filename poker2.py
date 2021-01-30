import random  #need for randomly selecting cards to use

lst_cards = ["2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "JD", "QD", "KD", "AD",
             "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "JH", "QH", "KH", "AH",
             "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "JC", "QC", "KC", "AC",            #List of all possible cards
             "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "JS", "QS", "KS", "AS",
             "XX"]

priority = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
            "J": 10, "Q": 11, "K": 12, "A": 1,                                  #Dictionary for assigning priority to each card
            "H": 999, "D": 555, "C": 333, "S": 1}



counter = 0 #counter to count up to 1000 as we are generating 1000 hands in this example

while counter < 1000:          #while loop to make sure 1000 hands are generated
    lst_selected_cards = []    #reset list of cards or otherwise the list will become 10,000 elements long


    while len(lst_selected_cards) < 10:   #ensures we only generate 10 cards per hand

        selected_card = lst_cards[random.randint(0, 47)]  # selection of random card from lst_cards

        if selected_card in lst_selected_cards:  #if the card selected is already in our selected cards list, then we ignore and choose again
            pass
        else:  #otherwise add it into our list
            lst_selected_cards.append(selected_card)

    counter_sandbox = 0  #new counter for splitting selected card list into two lists/hands
    hand_1 = []     #declaring new lists
    hand_2 = []

    for i in range(0, len(lst_selected_cards)):  #cycle through all the elements/cards in the list

        if counter_sandbox >= 5:
            hand_2.append(lst_selected_cards[i])    #when the for loop has run 5 times it will then add add the 6th --> 10th cards in the list to hand_2
        else:
            hand_1.append(lst_selected_cards[i])    #first five cards are added to hand_1

        counter_sandbox = counter_sandbox + 1   #counts how many times the loop has run


    for i in range(0, len(hand_1) - 1):     #cycling through all the elements in hand_1 -1 on the length to ensure no out of range error
        for j in range(0, len(hand_1) - 1 - i): #nested for loop, will ensure the bubble sort is repeated untill no more sorts need to be done
            temp_1 = list(hand_1[j])[0] #first letter/number in the hand
            temp_2 = list(hand_1[j])[1] #second letter/number in the hand
            temp_1_n = list(hand_1[j + 1])[0] #first letter/number in the next hand
            temp_2_n = list(hand_1[j + 1])[1] #second letter/number in the next hand

            if priority[temp_1] + priority[temp_2] < priority[temp_1_n] + priority[temp_2_n]:  #if statement that basically says if the priority of the current hand is less
                # print(hand_1[i], "<", hand_1[i + 1])                                         #than the next hand   (bubble sort)
                hand_1[j], hand_1[j + 1] = hand_1[j + 1], hand_1[j] #swapping the two hands

    for i in range(0, len(hand_2) - 1): #repeated process but for hand_2
        for j in range(0, len(hand_2) - 1 - i):
            temp_1 = list(hand_2[j])[0]
            temp_2 = list(hand_2[j])[1]
            temp_1_n = list(hand_2[j + 1])[0]
            temp_2_n = list(hand_2[j + 1])[1]

            if priority[temp_1] + priority[temp_2] < priority[temp_1_n] + priority[temp_2_n]:
                # print(hand_2[i], "<", hand_2[i + 1])
                hand_2[j], hand_2[j + 1] = hand_2[j + 1], hand_2[j]

    lst_selected_cards = hand_1 + hand_2  #combine the two hands into the form that will be stored into the file

    p_file = open("poker.txt", "a") #appending not writing
    p_file.write(lst_selected_cards[0] + " " +  lst_selected_cards[1] + " " + lst_selected_cards[2] + " " + lst_selected_cards[3]
                 + " " + lst_selected_cards[4] + " " + lst_selected_cards[5] + " " + lst_selected_cards[6] + " " + lst_selected_cards[7]   #formatting the input into the file
                 + " " + lst_selected_cards[8] + " " + lst_selected_cards [9] + "\n")

    p_file.close()
    counter = counter + 1 #one hand generated and sorted, now 999 to go if counter = 1

if counter == 1000:
    print(counter,"hands have been generated and ordered and appended to 'poker.txt' using these rules:\n1. Suits First --> Hearts Diamonds, Clubs, Spades.\n2. Value Second --> 9, 8, 7 etc...\n3. Ace Value --> Low ")
    #confirmation message


