def get_cocktail_hint(cocktail_name):
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
