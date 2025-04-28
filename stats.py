def get_word_count(string):
    words_array = string.split()
    return len(words_array)

def char_count(chars):
    characters = {}
    for char in chars:
        if (char.lower() not in characters):
            characters[char.lower()] = 1
        else:
            characters[char.lower()] += 1
    return characters

def sort_on(dict):
    return dict["num"]

def sort_dict_list(chars_dict):
    list = []
    for char in chars_dict:
        if char.isalpha():
            temp_dict = {"char": char, "num": chars_dict[char]}
            list.append(temp_dict)
    list.sort(reverse=True, key=sort_on)
    return list