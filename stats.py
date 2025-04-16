def get_word_count(text):
        words = text.split()
        num_words = len(words)
        return num_words


def get_letter_count(text):
	no_cap = text.lower()
	letter_dictionarie = {}
	for char in no_cap:
		if char in letter_dictionarie:
			letter_dictionarie[char] += 1
		else:
			letter_dictionarie[char] = 1
	return letter_dictionarie

def sort_char_count(char_counts):
    chars_list = []
    for char, count in char_counts.items():
        if char.isalpha():
            char_dict = {"char": char, "count": count}
            chars_list.append(char_dict)
    chars_list.sort(reverse=True, key=lambda x: x["count"])
    
    return chars_list
