def main():
    book_file_path = "books/frankenstein.txt"
    text = get_text(book_file_path)
    characters_countdict = charactercount(text)
    report(text,book_file_path,characters_countdict)


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
            elif letters.isalpha() == True:
                characters[letters] = 1
    return (dict(sorted(characters.items(), key=lambda x: x[1], reverse=True)))


def report(text,path,c_dict):
    print("\n-------Beginning of Report-------\n")
    print(f"Report of {path}")
    print(f"\nWord Count of book: {wordcount(text)}")


    print("\nBelow are the characters used (In order from most used to least used):")
    for c in c_dict:
        print(f"The Character '{c}' was used '{c_dict[c]}' times")


    print("\n-------End of Report-------\n")
            




main()