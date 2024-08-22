def main():
    book_file_path = "books/frankenstein.txt"
    text = get_text(book_file_path)
    print(text)
    print(f"Word Count: {wordcount(text)}")

def get_text(path):
    with open(path) as text:
        return text.read()



def wordcount(text):
    current_count = 0
    to_be_counted = text.split()
    for word in to_be_counted:
        current_count += 1
    return current_count

        






main()