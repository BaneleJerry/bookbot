def main():
    with open("books/Frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        word_count = len(words)

        print(f"--- Begin report of books/Frankenstein.txt ---")
        print(f"{word_count} words found in the document\n")

        char_count = count_letters(file_contents)
        print_character_counts(char_count)

        print("--- End report ---")

def count_letters(text):
    text_lower = text.lower()
    char_count = {}
    for char in text_lower:
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    return char_count

def print_character_counts(char_count):
    char_count = sorted(char_count.items())
    for char, count in char_count:
        print(f"The '{char}' character was found {count} times")

main()
