import os
from collections import Counter
import string

# Function that handles the absolute filepath
def get_file_path(filename: str) ->str:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

# Create a function that handles opening files
def open_file(path: str) -> str:
    filepath = get_file_path(path)

    try:
        with open(filepath, 'r') as file:
            text: str = file.read()
            return text

    except FileNotFoundError:
        print(f"Error, the file: '{path}' was not found at '{filepath}'")


# Create a function that analyses any string
def analyse(text: str) -> dict[str, int]:
    result: dict[str, int] = {
        'total_chars_incl_spaces': len(text),
        'total_chars_excl_spaces': len(text.replace(' ', '')),
        'total_spaces': text.count(' '),
        'total_words': len(text.split())
    }

    return result


# Count most frequent words
def get_most_common_words(text: str, top_n=5) -> list[tuple[str, int]]:
    clean_text = text.lower().translate(str.maketrans('', '', string.punctuation))
    words = clean_text.split()

    return Counter(words).most_common(top_n)

# Makes report human-readable
def display_report(analysis: dict, common_words: list) -> None:
    labels = {
        'total_chars_incl_spaces': "Total characters (with spaces)",
        'total_chars_excl_spaces': "Total characters (without spaces)",
        'total_spaces': "Amount of space",
        'total_words': "Word count"
    }

    print("--Text Analysis Report--")
    for key, description in labels.items():
        print(f"{description:<35}: {analysis.get(key)}")

    print("--Top 5 Most Common Words--")
    for word, count in common_words:
        print(f"{word}: is mentioned {count} times")

# Create a main entry point
def main() -> None:
    text: str = open_file(path='note.txt')

    if not text:
        return

    # Process data
    analysis_result = analyse(text)
    top_words = get_most_common_words(text)

    # Display results
    display_report(analysis_result, top_words)

# Run the script
if __name__ == '__main__':
    main()
