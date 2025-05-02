from stats import get_num_words, count_characters
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")
        book_data = get_book_text()
        num_words = get_num_words(book_data.split())
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for data in count_characters(book_data):
            print(f"{data['char']}: {data['num']}")
        print("============= END ===============")
