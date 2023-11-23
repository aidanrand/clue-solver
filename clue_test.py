import clue, random

personlist = clue.final_person_list.copy()
weaponlist = clue.final_weapon_list.copy()
roomlist = clue.final_room_list.copy()
answer = [random.choice(personlist), random.choice(weaponlist), random.choice(roomlist)]
personlist.remove(answer[0])
weaponlist.remove(answer[1])
roomlist.remove(answer[2])
numpeople = int(input("TEST: How many people are there? "))
usernum = random.randrange(numpeople)
print("You are player number " + str(usernum+1))
cardlist = personlist + weaponlist + roomlist
biglist = ["Players' cards"]
for i in range(numpeople):
    biglist.append([])
i = 1
while len(cardlist) > 0:
    if i > numpeople:
        i = 1
    card = random.choice(cardlist)
    biglist[i].append(card)
    cardlist.remove(card)
    i = i+1

for i in range(1, numpeople+1):
    print("Player "+str(i)+"'s cards: " + str(biglist[i]))

print("\nTesting Main Function Now....\n")
clue.main()
print(answer)
'''
def makeguess():
    person = random.choice(final_person_list)
    weapon = random.choice(final_weapon_list)
    room = random.choice(final_room_list)
    guess_list = (person, weapon, room)
    print("Guess:", guess_list)
    return guess_list
'''
