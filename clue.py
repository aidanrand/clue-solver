# Written by Aidan Rand, Last updated May 2023

final_person_list = ['Mustard', 'Plum', 'Green', 'Peacock', 'Scarlet', 'White', 'Rose', 'Gray', 'Brunette', 'Peach']
final_weapon_list = ['Knife', 'Candlestick', 'Revolver', 'Rope', 'Lead Pipe', 'Wrench', 'Poison', 'Horseshoe']
final_room_list = ['Courtyard', 'Drawing Room', 'Dining Room', 'Kitchen', 'Carriage House', 'Trophy Room',
                   'Conservatory', 'Studio', 'Billiard Room', 'Library']
original_dict = {'Mustard': None, 'Plum': None, 'Green': None, 'Peacock': None, 'Scarlet': None, 'White': None,
                 'Rose': None, 'Gray': None, 'Brunette': None, 'Peach': None, 'Knife': None, 'Candlestick': None,
                 'Revolver': None, 'Rope': None, 'Lead Pipe': None, 'Wrench': None, 'Poison': None, 'Horseshoe': None,
                 'Courtyard': None, 'Drawing Room': None, 'Dining Room': None, 'Kitchen': None, 'Carriage House': None,
                 'Trophy Room': None, 'Conservatory': None, 'Studio': None, 'Billiard Room': None, 'Library': None}

times_asked_about = {'Mustard': 0, 'Plum': 0, 'Green': 0, 'Peacock': 0, 'Scarlet': 0, 'White': 0, 'Rose': 0, 'Gray': 0,
                     'Brunette': 0, 'Peach': 0, 'Knife': 0, 'Candlestick': 0, 'Revolver': 0, 'Rope': 0, 'Lead Pipe': 0,
                     'Wrench': 0, 'Poison': 0, 'Horseshoe': 0, 'Courtyard': 0, 'Drawing Room': 0, 'Dining Room': 0,
                     'Kitchen': 0, 'Carriage House': 0, 'Trophy Room': 0, 'Conservatory': 0, 'Studio': 0,
                     'Billiard Room': 0, 'Library': 0}

person_list = final_person_list.copy()
weapon_list = final_weapon_list.copy()
room_list = final_room_list.copy()

player_list = []
dict_list = []
list_of_player_cards = []
num_card_list = []
cards_seen = []
cards_shown = []
game_over = False

turn_num = 1
round_num = 1
record_num = 1


def main():
    info_input()
    while not game_over:
        play_round()


def info_input():
    global num_opponents, user_number
    user_number = int(input("Enter your player number: "))
    num_opponents = int(input("Enter how many opponents you have: "))
    y = 1
    player_list.append("PLAYERS")
    dict_list.append("DICTLIST")
    list_of_player_cards.append("PLAYER CARD LIST")
    num_card_list.append("NUMBER OF CARDS")
    while y <= num_opponents+1:
        dict_list.append(original_dict.copy())
        list_of_player_cards.append([])
        player_name = input("Enter Player "+str(y)+"'s Name: ")
        player_list.append(player_name)
        if user_number == y:
            num_cards = int(input("Enter how many cards you have: "))
        else:
            num_cards = int(input("Enter how many cards they have: "))
        num_card_list.append(num_cards)
        y = y+1

    user_cards = num_card_list[user_number]
    z = 0
    while z < user_cards:
        input_card = input("Enter a Card you hold: ")
        while (final_person_list.count(input_card) == 0) and (final_weapon_list.count(input_card) == 0) and (final_room_list.count(input_card) == 0):
            input_card = input("Incorrect Spelling. Enter your card again: ")
        list_of_player_cards[user_number].append(input_card)
        remove_card(input_card)
        for i in range(1, num_opponents+2):
            if i == user_number:
                dict_list[user_number].update({input_card: "true"})
            else:
                update(i, input_card, "false")
        z = z+1


# updates a card's information in the dictionary to reflect new information
def update(index, card, value):
    if index != user_number:
        if (dict_list[index].get(card) == "true") or (dict_list[index].get(card) == "false"):
            return
        if value == "true":
            val = dict_list[index].get(card)
            dict_list[index].update({card: "true"})
            remove_card(card)
            list_of_player_cards[index].append(card)
            for i in range(1, num_opponents+2):
                if i != index:
                    dict_list[i].update({card: "false"})
            if (val is not None) and (val != "false"):
                for each in val:
                    for key in dict_list[index]:
                        val2 = dict_list[index].get(key)
                        if (val2 != "true") and (val2 != "false") and (val2 is not None):
                            if val2.count(each) == 1:
                                val2.remove(each)
                                dict_list[index].update({key: val2})
            return
        if value == "false":
            dict_list[index].update({card: "false"})
            return
        if dict_list[index].get(card) is None:
            dict_list[index].update({card: [value]})
            return
        possibility_list = dict_list[index].get(card)
        possibility_list.append(value)
        dict_list[index].update({card: possibility_list})
        return


def play_round():
    global turn_num, round_num, game_over
    turn_num = 1
    print("\n" + "Start of Round " + str(round_num) + "\n")
    while turn_num <= 1+num_opponents:
        set_others_to_false()
        if (len(person_list) * len(weapon_list) * len(room_list) <= 1) and (turn_num == user_number):
            game_over = True
            make_accusation()
            return
        if turn_num == user_number:
            user_guess()
        if turn_num != user_number:
            opponent_guess()
        for i in range(1, num_opponents+2):
            deduction(i)
        eliminate_solutions(final_person_list, person_list)
        eliminate_solutions(final_weapon_list, weapon_list)
        eliminate_solutions(final_room_list, room_list)
        set_others_to_true(final_person_list, person_list)
        set_others_to_true(final_weapon_list, weapon_list)
        set_others_to_true(final_room_list, room_list)
        turn_num = turn_num + 1
    round_num = round_num + 1


def user_guess():
    global record_num, question_num
    print("\n" + "Turn " + str(turn_num) + "\n")
    response = 'no'
    question_num = 1
    print_notebook()
    guess = guess_input()

    player_asked = turn_num + 1
    while ((response == 'no') or (response == 'No')) and (question_num <= num_opponents):
        if player_asked > num_opponents+1:
            player_asked = player_asked % (num_opponents+1)
        response = input("Enter "+player_list[player_asked] + "'s Response: ")
        while (response != "No") and (response != "no") and (response != "Yes") and (response != "yes"):
            response = input("Incorrect Response. Enter either 'No', 'no', 'Yes', or 'yes': ")
        question_num = question_num + 1
        if (response == "No") or (response == 'no'):
            update(player_asked, guess[0], "false")
            update(player_asked, guess[1], "false")
            update(player_asked, guess[2], "false")
            player_asked = player_asked + 1
    if player_asked > num_opponents + 1:
        player_asked = player_asked % (num_opponents + 1)
    if player_asked != user_number:
        card = input("Enter the Card "+player_list[player_asked]+" Showed You: ")
        while final_person_list.count(card) == 0 and final_weapon_list.count(card) == 0 and final_room_list.count(card) == 0:
            card = input("Incorrect Spelling. Enter the Card "+player_list[player_asked]+" Showed You Again: ")
        cards_seen.append(card)
        update(player_asked, card, "true")


def opponent_guess():
    global record_num, question_num
    print("\n" + "Turn " + str(turn_num) + "\n")
    response = 'no'
    question_num = 1
    print_notebook()
    guess = guess_input()

    player_asked = turn_num
    while ((response == 'no') or (response == 'No')) and (question_num <= num_opponents):
        player_asked = player_asked + 1
        if player_asked > (num_opponents+1):
            player_asked = player_asked % (num_opponents+1)
        response = input("Enter "+player_list[player_asked] + "'s Response: ")
        while (response != "No") and (response != "no") and (response != "Yes") and (response != "yes"):
            response = input("Incorrect Response. Enter either 'No', 'no', 'Yes', or 'yes': ")
        question_num = question_num + 1
        if (response == "No") or (response == 'no'):
            update(player_asked, guess[0], "false")
            update(player_asked, guess[1], "false")
            update(player_asked, guess[2], "false")
        if (response == "Yes") or (response == "yes"):
            if (dict_list[player_asked].get(guess[0]) == "true") or (dict_list[player_asked].get(guess[1]) == "true") or (dict_list[player_asked].get(guess[2]) == "true"):
                break
            update(player_asked, guess[0], str(record_num))
            update(player_asked, guess[1], str(record_num))
            update(player_asked, guess[2], str(record_num))
            record_num = record_num + 1
    if (player_asked == user_number) and ((response == 'yes') or (response == "Yes")):
        card = input("Enter the Card You Showed "+player_list[turn_num]+": ")
        while list_of_player_cards[user_number].count(card) == 0:
            card = input("Incorrect Spelling. Enter the Card You Showed "+player_list[turn_num]+" Again: ")
        cards_shown.append([card, player_list[turn_num]])


def remove_card(input_card):
    if input_card in person_list:
        person_list.remove(input_card)
        return
    if input_card in weapon_list:
        weapon_list.remove(input_card)
        return
    if input_card in room_list:
        room_list.remove(input_card)
        return


# if opponent A makes a guess and another opponent B shows them a card, they must have 1-3 of the cards guessed.
# if we learn that opponent B does not have 2 of the cards guessed, then they must have the remaining card
def deduction(index):
    testlist = []
    for each in dict_list[index].values():
        if (each != "false") and (each != "true") and (each is not None):
            for all in each:
                testlist.append(all)
    for j in testlist:
        if testlist.count(j) == 1:
            for all_keys in dict_list[index]:
                value1 = dict_list[index].get(all_keys)
                if (value1 != "false") and (value1 != "true") and (value1 is not None) and (value1.count(j) == 1):
                    temp_list = value1.remove(j)
                    update(index, all_keys, "true")
                    if temp_list is None:
                        break
                    for every in temp_list:
                        for total in dict_list[index]:
                            val = dict_list[index].get(total)
                            if (val.count(every) == 1) and len(val) > 1:
                                val.remove(every)
                                break
                            elif val.count(every) == 1:
                                dict_list[index].update({total: None})
                                break


# if no one has a card, it must be in the solution set
def eliminate_solutions(final_list, possibility_list):
    for each in final_list:
        remove_others = True
        for i in range(1, num_opponents + 2):
            if dict_list[i].get(each) != "false":
                remove_others = False
        if remove_others:
            for j in final_list:
                if (j != each) and (possibility_list.count(j) == 1):
                    possibility_list.remove(j)


def guess_input():
    player = player_list[turn_num] + "'s "
    if turn_num == user_number:
        player = "Your "
    person_guess = input("Enter "+player+"Person Guess: ")
    while final_person_list.count(person_guess) == 0:
        person_guess = input("Incorrect Spelling. Enter " + player + "Person Guess: ")
    weapon_guess = input("Enter "+player+"Weapon Guess: ")
    while final_weapon_list.count(weapon_guess) == 0:
        weapon_guess = input("Incorrect Spelling. Enter " + player + "Weapon Guess: ")
    room_guess = input("Enter "+player+"Room Guess: ")
    while final_room_list.count(room_guess) == 0:
        room_guess = input("Incorrect Spelling. Enter " + player + "Room Guess: ")
    val1 = times_asked_about.get(person_guess)
    val2 = times_asked_about.get(weapon_guess)
    val3 = times_asked_about.get(room_guess)
    times_asked_about.update({person_guess: val1 + 1})
    times_asked_about.update({weapon_guess: val2 + 1})
    times_asked_about.update({room_guess: val3 + 1})
    return [person_guess, weapon_guess, room_guess]


def print_notebook():
    if turn_num == user_number:
        for each in times_asked_about:
            print(each, "was asked about " + str(times_asked_about.get(each)) + " times")
    print("\nYour Cards:", list_of_player_cards[user_number])
    for i in range(1, num_opponents + 2):
        if i != user_number:
            print(player_list[i] + "'s Cards: ", list_of_player_cards[i])
    print("\n")
    for i in range(1, num_opponents + 2):
        print(player_list[i] + " Notes:", dict_list[i])

    print("\nCards You've Seen:", cards_seen)
    print("Cards You've Shown:", cards_shown)
    print("\nNumber of Solutions Remaining: "+str(len(person_list)*len(weapon_list)*len(room_list)) + " of 800")
    print("People Remaining:", person_list)
    print("Weapons Remaining:", weapon_list)
    print("Rooms Remaining:", room_list)


# shows solution when there is one person, weapon, and room remaining, and it is the user's turn
def make_accusation():
    print("\nMAKE ACCUSATION: ")
    print("PERSON:", person_list[0])
    print("WEAPON:", weapon_list[0])
    print("ROOM:", room_list[0])


# if a person has n cards, and their dictionary has n true values, all the rest of the values are false
def set_others_to_false():
    for i in range(1, num_opponents+2):
        count = 0
        for each in dict_list[i]:
            if dict_list[i].get(each) == "true":
                count = count+1
        if count == num_card_list[i]:
            for all in dict_list[i]:
                if dict_list[i].get(all) != "true":
                    dict_list[i].update({all: "false"})


# if either the person, weapon, or room is known, someone must have the other person, room, weapon, or room cards
def set_others_to_true(final_list, possibility_list):
    if len(possibility_list) != 1:
        return
    for each in final_list:
        if each != possibility_list[0]:
            set_true = True
            count = 0
            for i in range(1, num_opponents+2):
                if dict_list[i].get(each) == "true":
                    set_true = False
                if dict_list[i].get(each) == "false":
                    count = count + 1
            if (count == num_opponents) and set_true:
                for i in range(1, num_opponents+2):
                    if dict_list[i] != "false":
                        update(i, each, "true")
        else:
            for i in range(1, num_opponents + 2):
                if dict_list[i].get(each) != "false":
                    update(i, each, "false")


if __name__ == "__main__":
    main()
