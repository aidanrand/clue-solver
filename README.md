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
playing against three other people (4 total players), the number of opponents is 3. Players' names are not neccessary
for the solver, but it may help the user to keep track of things while the game is played. Make sure to input the names 
of players in the order they ask questions, and how many cards they were dealt. Then, input the cards you were dealt.