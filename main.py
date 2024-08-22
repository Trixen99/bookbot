def main():
    book_file_path = "books/frankenstein.txt"
    text = get_text(book_file_path)
    characters_countdict = charactercount(text)
    print(text)
    print(f"\nWord Count of book: {wordcount(text)}")
    print("\nBelow are the characters used in order from most used to least used:")
    for c in characters_countdict:
        print(f"{c} = {characters_countdict[c]}")


def get_text(path):
    with open(path) as text:
        return text.read()



def wordcount(text):
    current_count = 0
    to_be_counted = text.split()
    for word in to_be_counted:
        current_count += 1
    return current_count


def charactercount(booktext):
    characters = {}
    booktext = booktext.lower()
    booktext = booktext.split()
    for words in booktext:
        for letters in words:
            if letters in characters:
                characters[letters] += 1
            else:
                characters[letters] = 1
    return (dict(sorted(characters.items(), key=lambda x: x[1], reverse=True)))

            



        






main()