# CECS 551 Assignment 1

## Background
Consider a gameshow scenario where a contestant is asked to choose one of three boxes. Inside one box is a prize, and the other two boxes are empty. After the contestant makes an initial choice, the host, who knows the winning box, opens one of the two remaining boxes. The contestant is then given the option to stick with their original choice or switch to the other unopened box.

## Task:
You are to write a program that simulates this game show scenario multiple times (e.g., 10,000 simulations) to empirically determine the probability of winning the prize using the two strategies:

   
1. Switching to the other box after the host reveals an empty one.
   
2. Sticking with the initial box choice.

Before you start coding, consider your expectations of the odds for each strategy. Which one, if any, is better?

 

## Code Explanation
When you are ready to code, download `the_box.py` python file and write your code in the unfinished functions. 

## Class: `Guess_The_Box`
   
- **Description**: Simulates the game setup with three boxes, one containing a prize and the others empty.
   
- `__init__` Method initializes the game by shuffling the boxes to randomly assign the prize's location.
   
- `get_hint`  Method provides a hint by returning the index of one empty box not chosen by the player, simulating the host's action of revealing a non-prize box.
   
- Please do not change any code in this class.

## Implement the function: `play_the_game`
   
- Purpose: Executes a single game iteration using the specified strategy ("Switch" or "Hold").
   
- Input Argument: `strategy` - Determines whether the player switches their initial choice or holds onto it.
   
- Logic:        
           
  - Switch: The player initially randomly picks a box, after that using the `get_hint` function, the player receives a hint about an empty box, and switches to the remaining box. A win (1) is recorded if the new choice contains the prize. Otherwise, the function should return (0)
           
  - Hold: The player sticks with their initial random guess, recording a win if the box contains the prize (returns 1) otherwise, it records a loss (returns 0)
       
   
## Implement the function: `main`
   
- Objective: Run the simulation 10,000 times for each strategy to calculate winning probabilities.
   
- Process:        
           
  - Iterates through each strategy, simulating the game 10,000 times for each strategy.
           
  - Accumulates wins for each strategy to calculate success rates.
           
  - Prints calculated probabilities of winning for both strategies: "switch" and "hold", respectively.

## Conclusions
Make an empirical comparison between the "Switch" and "Hold" strategies.

Explain how the experiment confirms or contradicts your expectations.

Write your responses as a comment block in `thebox.py` file. Provide enough comments in your code so that someone reading it for the first time can understand it easily. 