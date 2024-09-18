"""
    Cocktail Connoisseur Hints Module

    This module provides functionalities to generate and deliver hints for cocktails in the 'Cocktail Connoisseur' game.
    It helps the player guess the correct cocktail name by offering hints, such as the number of words in the cocktail name
    and its first letter. The player can request hints up to a maximum number defined by the game rules.

    Functions:
    - get_cocktail_hint(cocktail_name): Generates a list of hints for the given cocktail name.
    - provide_hints(cocktail_name, max_hints): Offers hints to the player based on their request and limits the number of hints provided.
"""


def get_cocktail_hint(cocktail_name):
    """
       Generates hints for the given cocktail name.

       This function creates a list of hints that help the player guess the cocktail.
       The hints include the number of words in the cocktail name and the first letter
       of the cocktail name. These hints can assist the player in making a more informed guess.

       Args:
           cocktail_name (str): The name of the cocktail for which hints are being generated.

       Returns:
           list: A list of hints for the given cocktail.
    """
    length = f"The name of cocktail contains {len(cocktail_name.split(" "))}  word/s"
    first_letter = f"The first letter of cocktails name is '{cocktail_name[0].upper()}'"
    hints = [length, first_letter]
    return hints


def provide_hints(cocktail_name, max_hints):
    """
    Handles the process of asking the player if they would like a hint
    and providing hints from Wikipedia up to a maximum limit.

    Args:
    cocktail_wikipedia (str): Wikipedia title of the cocktail to fetch hints for.
    max_hints (int): Maximum number of hints to provide to the player. Default is 2.

    Returns:
    int: The number of hints used by the player.
    """
    hints_used = 0
    hints = get_cocktail_hint(cocktail_name)

    if not hints or len(hints) < max_hints:
        print("No hints available for this cocktail.")
        return hints_used

    while hints_used < max_hints:
        ask_hint = input("\n💡 Would you like a hint? (y/n): ").strip().lower()

        if ask_hint == 'y':
            if hints_used < len(hints):
                print(f"\n💡 Hint {hints_used + 1}: {hints[hints_used]}")
                hints_used += 1
            else:
                print("\n❌ No more hints available.")
                break
        elif ask_hint == 'n':
            break
        else:
            print("❌ Invalid input. Please enter 'y' or 'n'.")

    return hints_used
