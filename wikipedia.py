"""
Wikipedia Module
================

This module provides functionality to fetch and clean cocktail ingredients from Wikipedia.

Functions:
----------
- get_cocktail_ingredients(cocktail_wikipedia) -> list[str] | None:
    Fetches and cleans cocktail ingredients from the specified Wikipedia page.

Dependencies:
-------------
- requests
- bs4 BeautifulSoup: Used to fetch and parse Wikipedia pages.

Usage:
------
To fetch and clean cocktail ingredients, call the `get_cocktail_ingredients` function with the Wikipedia page title of the cocktail. The function returns a list of cleaned ingredients if found, otherwise None.


"""


import requests
from bs4 import BeautifulSoup


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
                        text = item.get_text().replace("\xa0", " ")
                        if text:
                            ingredients.append(text)

        return ingredients if ingredients else None
    except Exception as e:
        print(f"Error fetching ingredients: {e}")
        return None
