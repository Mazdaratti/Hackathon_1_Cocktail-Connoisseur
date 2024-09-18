"""
Prompts Module
==============

This module provides various prompt functions to interact with the user for setting up the game.

"""

import cocktails


def prompt_number_of_players():
    """
    Prompts the user to enter the number of players.

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
    Prompts each player to enter their name.

    Args:
        num_players (int): The number of players.

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
    Prompts the user to enter the number of rounds to play.

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
    Prompts the user to select a difficulty level.

    Returns:
        str: The selected difficulty level (easy, medium, or hard).
    """
    while True:
        level_selection = input("Choose a difficulty level (easy, medium, hard): ").strip().lower()
        if level_selection not in cocktails.cocktails:
            print("❌ Invalid input! Please choose easy, medium, or hard.")
        else:
            return level_selection
