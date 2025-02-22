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