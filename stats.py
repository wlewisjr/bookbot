def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    character_count = {}
    for char in text:
        char_lower = char.lower()
        if char_lower not in character_count:
            character_count[char_lower] = 1
        else:
            character_count[char_lower] += 1
    return character_count
def sort_on(dict):
    return dict["count"]

def sort_characters_by_count(char_dict):
    characters = []
    for item in char_dict:
        characters.append({"char": item, "count": char_dict[item]})
    characters.sort(reverse=True, key=sort_on)
    return characters
