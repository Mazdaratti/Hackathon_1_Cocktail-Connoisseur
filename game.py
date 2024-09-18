"""
    Cocktail Connoisseur Game Module

    This module provides functionality for a cocktail guessing game
    where players try to guess the name of a cocktail based on its ingredients.
"""


import random
from wikipedia import get_cocktail_ingredients_and_url
from cocktails import cocktails
from hints import provide_hints


def play_round(player, difficulty, used_cocktails):
    """
        Plays a single round of the game by selecting a random cocktail from the given difficulty.
        The player can request hints during the round, which will reduce their final score for the round.

        Args:
            player (str): The name of the player.
            difficulty (str): The selected difficulty level (easy, medium, hard).
            used_cocktails (set): A set of cocktails that have already been used in the current session.
        Returns:
            int: Points earned by the player in the round.
    """
    available_cocktails = [cocktail for cocktail in cocktails[difficulty] if cocktail['name'] not in used_cocktails]
    if not available_cocktails:
        print("No more unique cocktails available. Ending the game.")
        return 0

    cocktail_data = random.choice(available_cocktails)
    cocktail_name = cocktail_data["name"]
    cocktail_wikipedia = cocktail_data["wikipedia"]
    used_cocktails.add(cocktail_name)
    # Fetch and clean the ingredients and image from Wikipedia
    ingredients, image_url = get_cocktail_ingredients_and_url(cocktail_wikipedia)

    if ingredients is None:
        print(f"Could not find details for {cocktail_name}. Skipping...")
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
    score_penalty = 2 * hints_used  # Reduce score by 2 per hint used
    final_score = max(0.0, base_score - score_penalty)

    # Check if the guess is correct
    if guess.lower() == cocktail_name.lower():
        print(f"✅ Correct! The cocktail is {cocktail_name}. You earned {final_score} points.")
        print(f"🖼️ Here's a picture of the {cocktail_name}: {image_url}")
    else:
        print(f"❌ Wrong! The correct cocktail was {cocktail_name}.")
        print(f"🖼️ Here's a picture of the {cocktail_name}: {image_url}")
        return 0
    return final_score
