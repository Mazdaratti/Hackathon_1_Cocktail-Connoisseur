"""
    Cocktail Connoisseur Display Module

    This module contains functions to handle the display of game instructions
     and the winner celebration in the 'Cocktail Connoisseur' game.
    The functions are designed to enhance the user experience
    by providing colorful, formatted messages using the `colorama` library.
"""


from colorama import Fore, Style


def display_game_instructions():
    """
        Displays the game instructions for 'Cocktail Connoisseur'.

        This function prints out detailed instructions for playing the game,
        including how to play, the objective, scoring system, and useful tips
        for maximizing scores. The instructions are formatted using colored text
        to enhance readability and engagement.

        The instructions include:
         - The goal of the game.
        - How the scoring works.
        - Tips on when to use hints.
      """
    print(f"""
{Fore.BLUE}==================================================
     🍸 Welcome to *Cocktail Connoisseur* 🍸
=================================================={Style.RESET_ALL}

How to Play:
1. In each round, you will be given a list of ingredients for a cocktail.
2. Your task is to guess the name of the cocktail based on those ingredients.
3. If you're stuck, you can type 'hint' to get a clue, but using hints will reduce your score.
4. After making your guess, you'll find out if you're correct or not.

{Fore.GREEN}Game Objective:{Style.RESET_ALL}
🎯 Score as many points as possible by guessing cocktails correctly!

{Fore.YELLOW}Scoring:{Style.RESET_ALL}
✅ Correct guess without a hint: Full points!
💡 Correct guess after using hints: Reduced points.
❌ Wrong guess: No points for that round.

{Fore.RED}Tips:{Style.RESET_ALL}
🧠 Think carefully before using a hint — sometimes the ingredients might be all you need!😉:

{Fore.BLUE}=================================================={Style.RESET_ALL}
Let's get started!
""")


def celebrate_winner(players_scores):
    """
    Celebrates the winner(s) of the 'Cocktail Connoisseur' game.

    Handles the following cases:
    - One-player game:
        * If the player scores 0 points, they lose and a motivational message is displayed.
        * If the player scores more than 0 points, they win.
    - Multiplayer game:
        * If one player has the highest score, they win.
        * If multiple players tie for the highest score, they all win.
        * If all players score 0 points, it displays a motivational message.

    Args:
        players_scores (dict): A dictionary where the keys are player names
                               and the values are their corresponding scores.

    Returns:
        None
    """
    max_score = max(players_scores.values())
    winners = [player for player, score in players_scores.items() if score == max_score]
    total_players = len(players_scores)

    if total_players == 1:
        # Case: One-player game
        player = winners[0]  # Single player will always be in 'winners'
        if max_score == 0:
            # Player with 0 points (motivational message)
            print(f"""
        😅 Oh no, {player}! You scored 0 points! 😅
        🍹 Don't worry! Practice makes perfect. 🍹
        🔄 Why not try again and sharpen your cocktail knowledge? 🔄
        """)
        else:
            # Player with more than 0 points
            print(f"""{Fore.RED}
        🎉🎉🎉 CONGRATULATIONS {player}! 🎉🎉🎉{Style.RESET_ALL}
        🏆 You are the Cocktail Connoisseur Champion! 🏆
        🥂 You scored {max_score} points! 🥂
        🍾 Time to celebrate with your favorite drink! 🍾
        """)
    else:
        # Case: Multiplayer game
        if max_score == 0:
            # All players scored 0 points
            print(f"""
        😅 Oh no! It looks like all players scored 0 points! 😅
        🍹 Don't worry! Practice makes perfect. 🍹
        🔄 Why not try again and sharpen your cocktail knowledge? 🔄
        """)
        elif len(winners) == 1:
            # One winner
            winner = winners[0]
            print(f"""{Fore.RED}
        🎉🎉🎉 CONGRATULATIONS {winner}! 🎉🎉🎉{Style.RESET_ALL}
        🏆 You are the Cocktail Connoisseur Champion! 🏆
        🥂 You scored {players_scores[winner]} points! 🥂
        🍾 Time to celebrate with your favorite drink! 🍾
        """)
        else:
            # Multiple winners (tie)
            print(f"""
        🎉 It's a tie between {', '.join(winners)}! 🎉
        🏆 You all scored {max_score} points and are Cocktail Connoisseur Champions! 🏆
        🥂 Time to celebrate with your favorite drinks! 🥂
        """)

