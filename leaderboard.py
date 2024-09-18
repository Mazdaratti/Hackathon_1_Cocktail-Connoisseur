"""
    Cocktail Connoisseur Leaderboard Module

    This module provides functionality for displaying and saving a leaderboard for a game.
"""


from colorama import Fore, Style


def display_leaderboard(scores):
    """
        Displays the leaderboard with players' scores and announces the winner.

        Args:
            scores (dict): A dictionary with player names as keys and their scores as values.
    """
    print(f"{Fore.BLUE}\n=== Leaderboard ==={Style.RESET_ALL}")
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    for player, score in sorted_scores:
        print(f"{player}: {score} points")


def save_leaderboard(scores, filename="leaderboard.txt"):
    """
        Saves the leaderboard to a file.

        Args:
            scores (dict): A dictionary with player names as keys and their scores as values.
            filename (str): The name of the file to save the leaderboard to.
    """
    with open(filename, "a") as f:
        for player, score in scores.items():
            f.write(f"{player}: {score}\n")
