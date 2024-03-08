"""
Group Members:

╔═══════╦════════════════════════════╦════════════╗
║ Sr No ║            Name            ║ Student ID ║
╠═══════╬════════════════════════════╬════════════╣
║   1   ║ Tirth Shailesh Thoria      ║ 031149064  ║
║   2   ║ Avantika Singh             ║ 031376590  ║
║   3   ║ Laksh Chandrabhan Jadhwani ║ 032166249  ║
╚═══════╩════════════════════════════╩════════════╝

Before we code, let's outline what we expect from each approach -

1. Prediction for "Switch" Strategy -
	- The probability for a contestant to select the box containing the prize will be one in three.
	- After the host reveals a box without the prize, then it becomes more clear that the prize is in either of 2 boxes, one the contestant had initially chosen or the remaining unopened box.
	- Now, if the contestant switches his decision, then their probability of winning increases to two-thirds.
	- Expectation - We assume that the "switch" approach offers a greater chance of success than the "hold" approach.

2. Prediction for "Hold" Strategy -
	- The contestant decides not to change their decision.
	- And, the initial odds of the contestant winning was one in three.
	- Expectation - The "hold" approach offers a lesser chance of success than the "switch" approach.

Hence, we expect that the "switch" approach will exceed the "hold" approach with the help of the hint provided by the host, thereby improving the winning chance.

After conducting 10,000 simulations for each approach to compare the "Switch" and "Hold" methods empirically, the results supported the theoretical predictions:

1. Findings Regarding the "Switch" Method:
    - Based on the empirical data, using the "Switch" approach increased the chances of success.
    - This finding aligns with the theoretical prediction that increases the player's winning chances to two-thirds when the host switches doors after the reveal.
    - The "Switch" approach's higher winning odds, as demonstrated scientifically, support the Monty Hall dilemma's theoretical framework.

2. Findings Regarding the "Hold" Method:
    - Maintaining the "Hold" strategy resulted in a lower chance of success, according to the empirical data.
    - This finding is in line with the theoretical prediction that sticking with the first option without taking the host's hint into account results in decreased.

In conclusion, the empirical test between both the strategies approaches validates our theoretical expectations on the basis of the probability theory. The outcomes confirm that the "switch" decision increases our probability of winning more than the "hold" approach in the context of the Monty Hall problem, providing backing to the well-known probabilistic concept.
"""

import random


class Guess_The_Box:
    """
    The game class
    """

    def __init__(self) -> None:
        """Method initializes the game by shuffling the boxes to randomly assign the prize's location"""

        # Create a list of 3 boxes, one of which contains the prize
        box = ["Empty", "Empty", "Prize"]

        # Shuffle the boxes
        random.shuffle(box)

        # Assign the shuffled boxes to the class instance
        self.boxes = box

    def get_hint(self, guess: int) -> int:
        """
        Method provides a hint by returning the index of one empty box not chosen by the player, simulating the host's action of revealing a non-prize box.
        """

        # Get the indices of the empty boxes
        hints = [i for i, x in enumerate(self.boxes) if x == "Empty"]

        # Remove the player's guess from the list of hints
        if guess in hints:
            hints.remove(guess)

        # Return the first hint
        return hints[0]


def main() -> None:

    experiments = 10000  # Number of games to simulate
    probabilities = []  # List to store the win probabilities

    # Start the simulation
    for strategy in ["Switch", "Hold"]:
        wins = 0
        for _ in range(experiments):

            # Play the game and check if the player won
            if play_the_game(strategy):
                wins += 1

        # Calculate the win probability
        probabilities.append(wins / experiments)

    # Print the probability of 'Switch'
    print("Win probability when switching the choice:", probabilities[0])

    # Print the probability of 'Hold'
    print("Win probability when sticking with the choice:", probabilities[1])
    return


def play_the_game(strategy: str) -> bool:
    """Executes a single game iteration using the specified strategy ("Switch" or "Hold")

    `strategy`: Determines whether the player switches their initial choice or holds onto it
    """

    # Create an instance of the game
    game = Guess_The_Box()

    # Randomly choose a box from the 3 available
    initial_choice = random.randint(0, 2)

    # For the "Switch" strategy, the player switches to the remaining box
    if strategy == "Switch":

        # Get the index of the box to be revealed
        hint = game.get_hint(initial_choice)

        # Get the index of the remaining box
        new_choice = [0, 1, 2]

        # Remove the initial choice and the hint from the list of remaining boxes
        new_choice.remove(initial_choice)

        # Remove the hint from the list of remaining boxes
        new_choice.remove(hint)

        # The remaining box is the final choice
        final_choice = new_choice[0]

    # For the "Hold" strategy, the player sticks with their initial choice
    else:
        final_choice = initial_choice

    # Return whether the player won the game
    return game.boxes[final_choice] == "Prize"


if __name__ == "__main__":
    main()
