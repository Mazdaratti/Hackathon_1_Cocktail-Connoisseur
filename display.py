

from colorama import Fore, Style


def display_game_instructions():
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
            print(f"""{Fore.RED}
    🎉🎉🎉 CONGRATULATIONS {winner}! 🎉🎉🎉{Style.RESET_ALL}
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
