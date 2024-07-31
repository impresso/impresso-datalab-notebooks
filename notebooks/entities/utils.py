import requests

def get_wikipedia_page_props(input_str: str):
    """
    Retrieves the QID for a given Wikipedia page name from the specified language Wikipedia.
    If the request fails, it falls back to using the OpenRefine Wikidata API.

    Args:
        input_str (str): The input string in the format "page_name >> language".

    Returns:
        str: The QID or "NIL" if the QID is not found.
    """
    try:
        # Preprocess the input string
        page_name, language = input_str.split(" >> ")
        page_name = page_name.strip()
        language = language.strip()
    except ValueError:
        return "Invalid input format. Use 'page_name >> language'."

    wikipedia_url = f"https://{language}.wikipedia.org/w/api.php"
    wikipedia_params = {
        "action": "query",
        "prop": "pageprops",
        "format": "json",
        "titles": page_name,
    }

    qid = "NIL"
    try:
        # Attempt to fetch from Wikipedia API
        response = requests.get(wikipedia_url, params=wikipedia_params)
        response.raise_for_status()
        data = response.json()

        if "pages" in data["query"]:
            page_id = list(data["query"]["pages"].keys())[0]

            if "pageprops" in data["query"]["pages"][page_id]:
                page_props = data["query"]["pages"][page_id]["pageprops"]

                if "wikibase_item" in page_props:
                    # print("Found 'wikibase_item' in Wikipedia API response.")
                    return page_props["wikibase_item"]
                else:
                    # If no page properties found, fall back to OpenRefine Wikidata API
                    # print("No 'wikibase_item' found in Wikipedia API response.")

                    return qid  # fallback_to_openrefine(page_name, language)
            else:
                return qid  # fallback_to_openrefine(page_name, language)

    except Exception as e:
        # print(f"Error in Wikipedia API request: {e}")
        return qid  # fallback_to_openrefine(page_name, language)