"""
    Cocktail Connoisseur Main Game Module

    This module serves as the entry point for the multiplayer version of the 'Cocktail Connoisseur' game.
    It handles the main game loop, including player setup, round progression, score tracking, and winner celebration.
    The game involves multiple players taking turns to guess cocktails based on ingredients, with difficulty levels and
    rounds determined by player input.

    Functions:
    - play_game(): Runs the main game loop, manages player interactions, and calculates scores.
"""

from colorama import Fore, Style
from leaderboard import display_leaderboard, save_leaderboard
from prompts import prompt_number_of_players, prompt_player_names, prompt_number_of_rounds, prompt_difficulty
from display import display_game_instructions, celebrate_winner
from game import play_round


def play_game():
    """
    Runs the main game loop for a multiplayer game of "Cocktail Connoisseur".
    """
    display_game_instructions()

    # Get the number of players and their names
    num_players = prompt_number_of_players()
    players = prompt_player_names(num_players)

    # Prompt the user to select a difficulty level
    difficulty = prompt_difficulty()

    # Prompt the user to enter the number of rounds
    num_of_rounds = prompt_number_of_rounds()

    # Initialize the players' scores
    scores = {player: 0 for player in players}

    # Play the specified number of rounds
    for round_num in range(num_of_rounds):
        print(f"{Fore.BLUE}\n=== Round {round_num + 1} ==={Style.RESET_ALL}")
        for player in players:
            print(f"\n{player}'s turn:")
            scores[player] += play_round(player, difficulty)

    # Display and save the leaderboard,and announce the winner
    display_leaderboard(scores)
    save_leaderboard(scores)
    celebrate_winner(scores)


if __name__ == "__main__":
    play_game()
