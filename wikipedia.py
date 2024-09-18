"""
    Cocktail Connoisseur Wikipedia Ingredient and Image Fetcher

    This module provides a function to fetch and clean cocktail ingredients and retrieve the image URL
    from a cocktail's Wikipedia page using the BeautifulSoup library. The function sends an HTTP request
    to the Wikipedia page and extracts relevant information from the infobox.

    Functions:
    - get_cocktail_ingredients_and_url(cocktail_wikipedia): Fetches cocktail ingredients and image URL from Wikipedia.
"""


import requests
from bs4 import BeautifulSoup


def get_cocktail_ingredients_and_url(cocktail_wikipedia):
    """
        Fetches and cleans cocktail ingredients and image URL from a Wikipedia page.

        This function sends an HTTP GET request to the Wikipedia page of the specified cocktail.
        It uses BeautifulSoup to parse the page and extract ingredients listed in the infobox and
        the image URL, if available. The ingredients are cleaned to remove unnecessary characters.

        Args:
            cocktail_wikipedia (str): The Wikipedia page title for the cocktail.

        Returns:
            tuple: A tuple containing two elements:
                - A list of cleaned cocktail ingredients (list of str).
                - The image URL of the cocktail (str), or None if no image is found.

        Raises:
            HTTPError: If the request to Wikipedia fails.
            Exception: For any other exceptions encountered during the process.
    """
    try:
        url = f"https://en.wikipedia.org/wiki/{cocktail_wikipedia}"
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors

        soup = BeautifulSoup(response.text, 'html.parser')
        infobox = soup.find('table', {'class': 'infobox'})

        ingredients = []
        image_url = None

        if infobox:
            # Extract ingredients
            for row in infobox.find_all('tr'):
                header = row.find('th')
                if header and 'ingredients' in header.get_text().lower():
                    content = row.find('td')
                    if content:
                        for item in content.find_all(['li', 'p']):
                            text = item.get_text().strip()
                            if text:
                                ingredients.append(text)

            # Extract image URL
            img_tag = infobox.find('img')
            if img_tag:
                image_url = "https:" + img_tag['src']

        return ingredients, image_url

    except Exception as e:
        print(f"Error fetching details: {e}")
        return None, None
