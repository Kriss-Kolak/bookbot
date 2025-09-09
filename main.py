from stats import get_words, get_stats, sort_stats
import sys

def get_book_text(filepath):
    with open(filepath, 'r') as file:
        return file.read()
    

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    result = get_book_text(path)
    words = get_words(result)
    stats = get_stats(result)
    stats_list = sort_stats(stats)
    stats_list_string = ''
    for element in stats_list:
        stats_list_string = stats_list_string + f"{element['char']}: {element['num']}\n"
    print(
        f"============ BOOKBOT ============\n"
        f"Analyzing book found at {path}...\n"
        f"----------- Word Count ----------\n"
        f"Found {words} total words\n"
        f"--------- Character Count -------\n" +
        stats_list_string +
        f"============= END ===============\n"
        )


main()