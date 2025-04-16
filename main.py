import sys
from stats import get_word_count
from stats import get_letter_count
from stats import sort_char_count



def get_book_text(path_to_file):
	with open(path_to_file) as f:
		file_contents = f.read()
	return file_contents


def main():

	if len(sys.argv) < 2:
        	print("Usage: python3 main.py <path_to_book>")
        	sys.exit(1)

	book_path = sys.argv[1]

	book_text = get_book_text(book_path)
	word_count = get_word_count(book_text)
	letter_count = get_letter_count(book_text)
	report = sort_char_count(get_letter_count(book_text))
	print("========== BOOKBOT =========")
	print(f"Analyzing book found at {book_path}...")
	print("------- Word Count --------")
	print(f"Found {word_count} total words")
	print("------- Character Count ---")
	for char_dict in report:
		print(f"{char_dict['char']}: {char_dict['count']}")

main()


