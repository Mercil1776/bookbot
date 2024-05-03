def main():
    if book_path.endswith('.txt'):
        text = get_book_text(book_path)
        print(f"Reading the text in {book_path}...\n")
        count(text)
        print("Here are the characters in this text: ")
        counted_text = count_character(text)
        print_sorted(counted_text)
    else:
        raise Exception("Sorry! That is not a .txt file")

# Takes a filepath as input and returns the read text
def get_book_text(path):
    with open(path) as f:
        return f.read()

# Takes a body of text as input and prints the word count of the text
def count(t):
    word_count = len(t.split())
    print(f"There are {word_count} words in this text!\n")

# Takes a body of text as input and returns a dictionary of the amount of times each character appeares
def count_character(t):
    characters = {}
    for i in t:
        lowered = i.lower()
        if lowered in characters:
            characters[lowered] += 1
        else:
            characters[lowered] = 1
    return characters

# Takes a dictionary and prints out the amount of times each letter was found
def print_sorted(dict):
    list_characters = []
    for char, num in dict.items():
        char_pair = {char : num}
        list_characters.append(char_pair)
    list_characters.sort(reverse=True, key=lambda x: list(x.values())[0])
    for i in list_characters:
        for x, y in i.items():
            if x.isalpha():
                print(f"The '{x}' character was found {y} times")


book_path = "books/frankenstein.txt"
main()