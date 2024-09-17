import requests
from bs4 import BeautifulSoup
import random
from cocktails import cocktails


def display_game_instructions():
    print("""
==================================================
🍸 Welcome to *Cocktail Connoisseur* 🍸
==================================================

How to Play:
1. In each round, you will be given a list of ingredients for a cocktail.
2. Your task is to guess the name of the cocktail based on those ingredients.
3. If you're stuck, you can type 'hint' to get a clue, but using hints will reduce your score.
4. After making your guess, you'll find out if you're correct or not.

Game Objective:
🎯 Score as many points as possible by guessing cocktails correctly!

Scoring:
✅ Correct guess without a hint: Full points!
💡 Correct guess after using hints: Reduced points.
❌ Wrong guess: No points for that round.

Tips:
🧠 Think carefully before using a hint—sometimes the ingredients might be all you need!

==================================================
Let's get started!
""")


def get_cocktail_ingredients(cocktail_wikipedia):
    """
    Fetches and cleans cocktail ingredients from Wikipedia.

    Args:
        cocktail_wikipedia (str): The Wikipedia page title for the cocktail.

    Returns:
        list: A list of cleaned ingredients if found, otherwise None.
    """
    try:
        url = f"https://en.wikipedia.org/wiki/{cocktail_wikipedia}"
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors

        soup = BeautifulSoup(response.text, 'html.parser')
        infobox = soup.find('table', {'class': 'infobox'})

        if not infobox:
            return None

        ingredients = []
        for row in infobox.find_all('tr'):
            header = row.find('th')
            if header and 'ingredients' in header.get_text().lower():
                content = row.find('td')
                if content:
                    for item in content.find_all(['li', 'p']):
                        text = item.get_text(strip=True)
                        if text:
                            ingredients.append(text)

        return ingredients if ingredients else None
    except Exception as e:
        print(f"Error fetching ingredients: {e}")
        return None


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

    if not hints:
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


def get_number_of_players():
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


def get_player_names(num_players):
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


def get_number_of_rounds():
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
        if level_selection not in cocktails:
            print("❌ Invalid input! Please choose easy, medium, or hard.")
        else:
            return level_selection


def display_leaderboard(scores):
    """
    Displays the leaderboard with players' scores and announces the winner.

    Args:
        scores (dict): A dictionary with player names as keys and their scores as values.
    """
    print("\n=== Leaderboard ===")
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    for player, score in sorted_scores:
        print(f"{player}: {score} points")


def celebrate_winner(players_scores):
    # Find the player(s) with the highest score
    max_score = max(players_scores.values())
    winners = [player for player, score in players_scores.items() if score == max_score]

    if len(winners) == 1:
        winner = winners[0]
        if players_scores[winner] == 0:
            print(f"""
    😅 Oh no, {winner}! It looks like you scored 0 points. 😅
    🍹 Don't worry! Practice makes perfect. 🍹
    🔄 Why not try again and sharpen your cocktail knowledge? 🔄
    """)
        else:
            print(f"""
    🎉🎉🎉 CONGRATULATIONS {winner}! 🎉🎉🎉
    🏆 You are the Cocktail Connoisseur Champion! 🏆
    🥂 You scored {players_scores[winner]} points! 🥂
    🍾 Time to celebrate with your favorite drink! 🍾
    """)
    else:
        print(f"""
    🎉 It's a tie between {', '.join(winners)}! 🎉
    🍸 You all are Cocktail Connoisseur Champions! 🍸
    🥂 Time to celebrate with your favorite drinks! 🥂
    """)


def play_game():
    """
    Runs the main game loop for a multiplayer game of "Cocktail Connoisseur".
    """
    display_game_instructions()

    # Get the number of players and their names
    num_players = get_number_of_players()
    players = get_player_names(num_players)

    # Prompt the user to select a difficulty level
    difficulty = prompt_difficulty()

    # Prompt the user to enter the number of rounds
    num_of_rounds = get_number_of_rounds()

    # Initialize the players' scores
    scores = {player: 0 for player in players}

    # Play the specified number of rounds
    for round_num in range(num_of_rounds):
        print(f"\n=== Round {round_num + 1} ===")
        for player in players:
            print(f"\n{player}'s turn:")
            scores[player] += play_round(player, difficulty)

    # Display the leaderboard and announce the winner
    display_leaderboard(scores)
    celebrate_winner(scores)


if __name__ == "__main__":
    play_game()
