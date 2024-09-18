"""
Cocktail Guessing Game Module
=============================

This module provides functionality for a cocktail guessing game where players try to guess the name of a cocktail based on its ingredients.
"""


import random
from wikipedia import get_cocktail_ingredients
from cocktails import cocktails
from hints import provide_hints


def play_round(player, difficulty):
    """
    Plays a single round of the game by selecting a random cocktail from the given difficulty.
    The player can request hints during the round, which will reduce their final score for the round.

    Args:
        player (str): The name of the player.
        difficulty (str): The selected difficulty level (easy, medium, hard).

    Returns:
        int: Points earned by the player in the round.
    """
    cocktail_data = random.choice(cocktails[difficulty])
    cocktail_name = cocktail_data["name"]
    cocktail_wikipedia = cocktail_data["wikipedia"]

    # Fetch and clean the ingredients from Wikipedia
    ingredients = get_cocktail_ingredients(cocktail_wikipedia)

    if ingredients is None:
        print(f"Could not find ingredients for {cocktail_name}. Skipping...")
        return 0

    print(f"\n{player}, here are the ingredients for this cocktail:\n")
    for ingredient in ingredients:
        print(f"- {ingredient}")

    # Allow player to request hints
    max_hints = 2
    hints_used = provide_hints(cocktail_name, max_hints)

    # Get the player's guess
    guess = input("\n🧠 Guess the cocktail: ").strip()

    # Calculate score with penalty for hints used
    base_score = 10  # Full point for a correct guess
    score_penalty = 2 * hints_used  # Reduce score by 0.5 per hint used
    final_score = max(0.0, base_score - score_penalty)

    # Check if the guess is correct
    if guess.lower() == cocktail_name.lower():
        print(f"✅ Correct! The cocktail is {cocktail_name}. You earned {final_score} points.")
        return final_score  # Return points based on hints used
    else:
        print(f"❌ Wrong! The correct cocktail was {cocktail_name}.")
        return 0  # No points for a wrong guess
