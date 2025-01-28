import random

list_of_anagrams = {
    5: [
        ["abets", "baste", "betas", "beast", "beats"],
        ["acres", "cares", "races", "scare"],
        ["alert", "alter", "later"],
        ["angel", "angle", "glean"],
        ["baker", "brake", "break"],
        ["bared", "beard", "bread", "debar"],
        ["dater", "rated", "trade", "tread"],
        ["below", "bowel", "elbow"],
        ["caret", "cater", "crate", "trace", "react"]
    ],
    6: [
        ["arrest", "rarest", "raster", "raters", "starer"],
        ["carets", "caters", "caster", "crates", "reacts", "recast", "traces"],
        ["canter", "nectar", "recant", "trance"],
        ["danger", "gander", "garden", "ranged"],
        ["daters", "trades", "treads", "stared"]
    ],
    7: [
        ["allergy", "gallery", "largely", "regally"],
        ["aspired", "despair", "diapers", "praised"],
        ["claimed", "decimal", "declaim", "medical"],
        ["dearths", "hardest", "hatreds", "threads", "trashed"],
        ["detains", "instead", "sainted", "stained"]
    ],
    8: [
        ["parroted", "predator", "prorated", "teardrop"],
        ["repaints", "painters", "pantries", "pertains"],
        ["restrain", "retrains", "strainer", "terrains", "trainers"],
        ["construe", "counters", "recounts", "trounces"]
    ]
}

def get_random_word_and_count(word_length, word_length_lists=None):
    # Generate `word_length_lists` only if not provided
    if word_length_lists is None:  
        word_length_lists = list_of_anagrams[int(word_length)]

    random_list_index = random.randint(0, len(word_length_lists) - 1)
    selected_list = word_length_lists[random_list_index]
    random_word_index = random.randint(0, len(selected_list) - 1)
    random_word = selected_list[random_word_index]
    remaining_words_count = len(selected_list) - 1

    return word_length_lists, selected_list, random_word, remaining_words_count