def get_num_words(strings):
    words = strings.split()
    return len(words)

def character_count(strings):
    dictionary = {}
    for character in strings.lower():
        if character in dictionary.keys():
            dictionary[character] += 1
        else:
            dictionary[character] = 1
    return dictionary

def sorted_list(dictionary):
    character_list = []
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    for character in sorted_dict:
        if character.isalpha():
            character_list.append({"char":character, "num": sorted_dict[character]})
    return character_list
