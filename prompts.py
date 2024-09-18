"""
    Cocktail Connoisseur Prompts Module

    This module provides prompt functions to interact with the player for gathering essential game settings,
    such as the number of players, player names, the number of rounds, and the game's difficulty level.
    These prompts form the basis for setting up the multiplayer game of 'Cocktail Connoisseur'.

    Functions:
    - prompt_number_of_players(): Prompts the user to input the number of players.
    - prompt_player_names(num_players): Prompts the user to input each player's name.
    - prompt_number_of_rounds(): Prompts the user to input the number of rounds to play.
    - prompt_difficulty(): Prompts the user to choose a difficulty level for the game.
"""

import cocktails


def prompt_number_of_players():
    """
        Prompts the user to enter the number of players for the game.

        Continuously asks the user to provide the number of players until a valid positive integer is entered.
        If the user enters an invalid input (e.g., a non-numeric or non-positive value), an error message is displayed,
        and the user is prompted again.

        Returns:
            int: The number of players chosen by the user.
    """
    while True:
        players_selection = input("Enter the number of players: ").strip()
        try:
            num_of_players = int(players_selection)
            if num_of_players > 0:
                return num_of_players
            print("❌ Invalid input! Please enter a positive number.")
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")


def prompt_player_names(num_players):
    """
        Prompts each player to enter their name based on the number of players.

        Continuously prompts for each player's name, storing and returning them in a list.
        The number of player names requested is based on the `num_players` argument.

        Args:
            num_players (int): The number of players in the game.

        Returns:
            list: A list of player names.
    """
    players = []
    for i in range(num_players):
        name = input(f"Enter the name for player {i + 1}: ").strip()
        players.append(name)
    return players


def prompt_number_of_rounds():
    """
        Prompts the user to enter the number of rounds to play in the game.

        Continuously asks the user to provide the number of rounds until a valid positive integer is entered.
        If the user enters an invalid input, such as a non-numeric or non-positive value, an error message
        is displayed, and the user is prompted again.

        Returns:
            int: The number of rounds chosen by the user.
    """
    while True:
        rounds_selection = input("Enter the number of rounds: ").strip()
        try:
            num_of_rounds = int(rounds_selection)
            if num_of_rounds > 0:
                return num_of_rounds
            print("❌ Invalid input! Please enter a positive number.")
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")


def prompt_difficulty():
    """
        Prompts the user to select a difficulty level for the game.

        Continuously asks the user to select a difficulty level (easy, medium, or hard) until a valid option is chosen.
        If an invalid input is entered, an error message is displayed, and the user is prompted again.

        Returns:
            str: The selected difficulty level (easy, medium, or hard).
    """
    while True:
        level_selection = input("Choose a difficulty level (easy, medium, hard): ").strip().lower()
        if level_selection not in cocktails.cocktails:
            print("❌ Invalid input! Please choose easy, medium, or hard.")
        else:
            return level_selection
