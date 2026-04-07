# Import the necessary functionality
from collections import Counter
import re
import pypdf
from docx import Document
import os

STOPWORDS = {"el", "la", "los", "las", "un", "una", "de", "del", "que", "y", "en", "a", "con", "por", "para", "the", "be", "and", "of", "a" ,"in", "to", "have", "it", "I"}

# Create a function for getting the word frequency in text
def get_frequency(text: str, top_n: int = 10) -> list[tuple[str, int]]:
    if not text: return[]

    # Convert text to lowercase to ensure case-insensitivity
    lowered_text: str = text.lower()

    # Use regular expression to find all words (alphanumeric and underscore)
    words = re.findall(r'\b[a-zñáéíóú]+\b', lowered_text)

    filtered_words = [w for w in words if w not in STOPWORDS]

    # Count word frequencies using Counter
    word_counts: Counter = Counter(words)

    # Return the most common words as a tuple
    return Counter(filtered_words).most_common(top_n)


def read_file(file_path: str) -> str:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    _, file_extension = os.path.splitext(file_path)
    file_extension = file_extension.lower()
    chunks = []

    try:
        if file_extension == ".txt":
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()

        elif file_extension == ".pdf":
            reader = pypdf.PdfReader(file_path)
            for page in reader.pages:
                chunks.append(page.extract_text() or "")
        
        elif file_extension == ".docx":
            doc = Document(file_path)
            for para in doc.paragraphs:
                chunks.append(para.text)
        
        else:
            raise ValueError(f"Format {file_extension} not supporte")

    except Exception as e:
        raise RuntimeError(f"Proccesed Error {file_extension}: {e}")

    return "\n".join(chunks)


# Create a main entry point
def main() -> None:
    file_path = input('Enter your file path: ').strip()

    try:
        content = read_file(file_path)
        # Top-15 for a complete report
        frequencies = get_frequency(content, top_n=15)

        print(f"\n--- Analysis Results for: {os.path.basename(file_path)} ---")
        if not frequencies:
            print("Not meaningful words found")
        for word, count in frequencies:
            print(f"{word:15}: {count}") # Column formating with f-strings

    except Exception as e:
        print(f"ERROR: {e}")

# Run the script
if __name__ == "__main__":
    main()
