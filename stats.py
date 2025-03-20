def get_num_words(file_contents):
    file_list = file_contents.split()
    return len(file_list)  # Return just the count


def count_letters(file_contents):
    frequency = {}
    file_lower = file_contents.lower()
    for c in set(file_lower):
        if c.isalpha():  # Include only alphabetic characters
            frequency[c] = file_lower.count(c)
    return frequency


def sort_character_counts(char_dict):
    # Create a list of dictionaries from the char_dict
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "count": count})
    
    # Sort the list by count (greatest to least)
    # You'll need a helper function like in the hint
    def sort_on(dict):
        return dict["count"]
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list