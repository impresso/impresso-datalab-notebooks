import requests
from spacy import displacy


def get_linked_entities(text):
    url = "https://impresso-annotation.epfl.ch/api/ner_nel/"

    # Prepare the payload
    payload = {"data": text}

    try:
        # Make the POST request
        response = requests.post(url, json=payload)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the response JSON to get linked entities
            data = response.json()
            return data
        else:
            print(f"Request failed with status code {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return e


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




def prepare_entities_for_displacy(text, coarse_entities, fine_entities):
    """
    Prepare entities for stacked visualization in SpaCy's displacy.
    :param text: The original text.
    :param coarse_entities: Coarse-grained entities.
    :param fine_entities: Fine-grained entities.
    :return: A dictionary compatible with displacy for rendering.
    """
    combined_entities = []

    # Add coarse entities first
    for ent in coarse_entities:
        combined_entities.append(
            {
                "start": ent["start"],
                "end": ent["end"],
                "label": ent["entity"] + " (COARSE)",
            }
        )

    # Add fine entities on the same spans (stacked)
    for ent in fine_entities:
        combined_entities.append(
            {
                "start": ent["start"],
                "end": ent["end"],
                "label": ent["entity"] + " (FINE)",
            }
        )

    # Prepare data for displacy
    displacy_data = {"text": text, "ents": combined_entities, "title": None}

    return displacy_data


def visualize_stacked_entities(text, coarse_entities, fine_entities):
    """
    Visualize stacked coarse and fine-grained named entities using displacy.
    :param text: The original text.
    :param coarse_entities: Coarse-grained entities.
    :param fine_entities: Fine-grained entities.
    """
    print(f"\nVisualizing stacked coarse and fine-grained entities\n")

    # Prepare the combined entity data
    displacy_data = prepare_entities_for_displacy(text, coarse_entities, fine_entities)

    # Use displacy to render the entities in manual mode
    displacy.render(displacy_data, style="ent", manual=True, jupyter=True)


def print_nicely(results, text):
    for key, entities in results.items():
        if entities:
            print(f"\n**{key}**\n")
            print(
                f"{'Entity':<25} {'Type':<20} {'Score':<8} {'Index':<5} {'Word':<20} {'Start':<5} {'End':<5}"
            )
            print("-" * 70)
            for entity in entities:
                print(
                    f"{entity['word']:<25} {entity['entity']:<20} {entity['score']:<8.2f}% {entity['index'][0]:<5} {entity['word']:<20} {entity['start']:<5} {entity['end']:<5}"
                )
                # print(f"{text[entity['start']:entity['end']]:<15} {entity['entity']:<10} {entity['score']:<8.2f}% {entity['index'][0]:<5} {entity['word']:<20} {entity['start']:<5} {entity['end']:<5}")


def add_entity_tags(text, results):
    entities = []
    for task, ents in results.items():
        for entity in ents:
            entities.append((entity["start"], entity["end"], entity["word"]))

    already_done = []
    # Insert tags in the text using replace method
    for start, end, word in entities:
        if word not in already_done:
            text = text.replace(word, f"[START] {word} [END]")
            already_done.append(word)

    return text
