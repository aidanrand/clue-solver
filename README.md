# clue-solver

This is a solver for the popular Hasbro game Clue (named Cluedo internationally). It simulates the game, and takes in 
user input to record the questions players ask, their responses, and cards seen. Using this information, it deduces 
which players have which cards to determine the game's solution. In other words, the cards not held by any player must 
be the person, weapon, and room cards in the middle of the board. It simulates the process of filling out the "detective 
notebook", a piece of paper that players can use to take notes about the game in hopes of figuring out the solution and 
winning the game. 

clue.py is the main file for running the solver. Run this file, and it will start to take in user input about the game.
Your user number is what position you ask questions. If you ask questions first, your user number is 1, if you ask 
questions second, your user number is 2, and so on. The number of opponents does not include the user, so if you are 
playing against three other people (4 total players), the number of opponents is 3. Players' names are not necessary
for the solver, but it may help the user to keep track of things while the game is played. Make sure to input the names 
of players in the order they ask questions, and how many cards they were dealt. Then, input the cards you were dealt and 
the game will start. On the user's turn, the detective notebook will be printed to the console, represented by a 
dictionary for each player. For each player's dictionary, the keys are the cards, and the values are either true 
(meaning the player has that card), false (meaning that the player does not have that card), or a list of integers. If 
the value is a list, then each specific integer represents that card asked on a specific question. Therefore, cards with 
the same integer in their list represents being asked about together in the same question.

clue_test.py is the testing file for debugging purposes. It can also be used to shuffle the cards, pick a person, 
weapon, and room card for the solution, and deal the remaining cards to players. At the end of the game, it will display
the solution to the user.
